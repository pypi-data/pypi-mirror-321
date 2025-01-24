# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import datetime
import json
import logging
import socket
import urllib.request
from typing import Any
from uuid import UUID

from majormode.perseus.constant.http import HttpMethod
from majormode.perseus.constant.notification import DevicePlatform
from majormode.perseus.constant.notification import NotificationMode
from majormode.perseus.constant.obj import ObjectStatus
from majormode.perseus.constant.sort_order import SortOrder
from majormode.perseus.model import obj
from majormode.perseus.model.date import ISO8601DateTime
from majormode.perseus.model.notification import Notification
from majormode.perseus.utils import cast
from majormode.perseus.utils.rdbms import RdbmsConnection

from majormode.perseus.service.application.application_service import ApplicationService
from majormode.perseus.service.base_rdbms_service import BaseRdbmsService


class NotificationService(BaseRdbmsService):
    """
    A notification is a lightweight message that needs to be delivered to
    one or more recipients.  It informs the recipients about an event
    that occurs, which might require fetching additional data from the
    server platform or requesting the recipient to perform some action.

    A recipient is generally a client application that acts on behalf of a
    user, but it could also be an agent or botnet that controls a device.

    A message can be delivered to a recipient using different styles of
    network communication:

    - ``email``: the message is delivered in an Internet electronic mail
      message to the specified recipients based on a store-and-forward
      model.

    - ``push``: the message is delivered to the specified recipients
      when the request for the transmission of information is initiated
      by the publisher or server platform and pushed out to the receiver
      or client application.

    - ``pull``: the message is delivered to the specified recipients
      when the request for the transmission of information is initiated
      by the receiver or client application, and then is responded by the
      publisher or server platform.  Push style requires recipients to
      register with the server platform before it can receive messages
      using this mode.
    """

    # Default and maximum durations, expressed in seconds, during which
    # information of the notification reasonably may be expected usefully
    # to inform an action or interest of the intended recipient.  After
    # the lifespan expires, provision of the notification to the intended
    # recipients may be prevented.
    DEFAULT_LIFESPAN = 24 * 60 * 60  # 1 day
    MAXIMUM_LIFESPAN = 4 * 7 * 24 * 60 * 60  # 4 weeks

    # Define the host name of the Google Cloud Messaging for Android, a
    # free service that helps developers send data from servers to their
    # Android applications on Android devices, and upstream messages from
    # the user's device back to the cloud.  This could be a lightweight
    # message telling the Android application that there is new data to be
    # fetched from the server (for instance, a "new email" notification
    # informing the application that it is out of sync with the back end),
    # or it could be a message containing up to 4kb of payload data (so
    # apps like instant messaging can consume the message directly).  The
    # GCM service handles all aspects of queueing of messages and delivery
    # to the target Android application running on the target device.
    GCM_SERVER_HTTP_URL = 'https://gcm-http.googleapis.com/gcm/send'

    # Firebase Cloud Messaging
    #
    # Content-Type: application/json
    # Authorization: key=
    FCM_SERVER_HTTP_URL = 'https://fcm.googleapis.com/fcm/send'


    def __filter_already_notified_recipients(
            self,
            notification_type: str,
            recipient_ids: list[str],
            connection: RdbmsConnection = None,
            sender_id: str = None) -> list[str]:
        """
        Return the list of recipients who already received a similar
        notification.


        :param notification_type: The type of the notification to be sent, such
            as for instance `on_something_happened`.

        :param recipient_ids: The identifier of a recipient, or a list of
            identifiers of recipients, to send the notification to.

        :param connection: A connection to the notification database.

        :param sender_id: The identifier of the sender on behalf whom the
            notification is sent to the recipients.


        :return: The list of recipients who have already received a similar
            notification.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                '''
                SELECT DISTINCT 
                    recipient_id
                  FROM 
                    notification
                  WHERE
                    notification_type = %(notification_type)s
                    AND recipient_id IN (%[recipient_ids]s)
                    AND (%(sender_id)s IS NULL OR sender_id = %(sender_id)s)
                    AND NOT is_read
                ''',
                {
                    'notification_type': notification_type,
                    'recipient_ids': recipient_ids,
                    'sender_id': sender_id,
                }
            )

            recipient_ids = [
                row.get_value('recipient_id')
                for row in cursor.fetch_all()
            ]

            return recipient_ids

    def __get_device_registration(
            self,
            device_id: str,
            app_id: UUID,
            account_id: UUID = None,
            connection: RdbmsConnection = None):
        """
        Return the registration of a mobile device to the push notification
        service


        :param device_id: Identification of a mobile device that registered
            to push notification service.

        :param app_id: Identification of the mobile application that
            registered the mobile device to push notification service.

        :param account_id: Identification of the account of a user who
            registered his mobile device to push notification service.

        :param connection: A connection to the notification database.


        :return: An object containing the following attributes:

            - ``account_id: UUID` (optional): The account identifier of the user who
              registered his mobile device to push notification service.

            - ``app_id: UUID`` (required): The identifier of the client application
              that registered the mobile device to the push notification service.

            - ``device_id: str`` (required): The identifier of the mobile device.

            - ``device_platform: DevicePlatform`` (required): The mobile platform
              of the device.

            - ``device_token: str`` (required): The token that identifies the
              mobile device by the push notification provider of the device
              platform.

            - ``language: Locale`` (optional): The preferred language to receive
              message's textual content in.  This argument is not defined if the
              device registered to push notification service on behalf of a user.
              The preferred language of this user would be actually used>

            - ``object_status: ObjectStatus`` (required): The current status of the
              registration of this device to the push notification service.

            - ``registration_id: UUID`` (required): The identifier of the
              registration of the mobile device to the push notification service.

            - ``update_time: ISO8601DateTime`` (required): The time of the most
              recent modification of the properties of the mobile device's
              registration to the push notification service.
        """
        with self.acquire_rdbms_connection(auto_commit=False, connection=connection) as connection:
            cursor = connection.execute(
                '''
                SELECT
                    account_id,
                    app_id,
                    device_id,
                    device_platform,
                    device_token,
                    object_status,
                    registration_id,
                    update_time
                  FROM 
                    notification_device
                  WHERE
                    device_id = %(device_id)s
                    AND (
                      (account_id IS NULL AND %(account_id)s IS NULL)
                      OR account_id = %(account_id)s
                    )
                    AND app_id = %(app_id)s
                ''',
                {
                    'account_id': account_id,
                    'app_id': app_id,
                    'device_id': device_id,
                }
            )

            row = cursor.fetch_one()

            device_registration = row and row.get_object({
                'account_id': cast.string_to_uuid,
                'app_id': cast.string_to_uuid,
                'device_platform': DevicePlatform,
                'language': cast.string_to_locale,
                'object_status': ObjectStatus,
                'registration_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
            })

            return device_registration

    def __register_device(
            self,
            device_id: str,
            device_platform,
            app_id: UUID,
            device_token: str,
            account_id: UUID = None,
            connection: RdbmsConnection = None
    ) -> any:
        """
        Register a mobile device to the push notification service.


        :param device_id: The identifier of a mobile device that registers
            to push notification service.

        :param device_platform: The mobile platform of the device.

        :param app_id: The identifier of the client application that registers
            the mobile device to the push notification service.

        :param device_token: A token that identifies the device by the push
            notification provider of the device platform.

        :param account_id: The identifier of the account of a user who
            registers his mobile device to the push notification service.

        :param connection: A connection to the notification database.


        :return: An object containing the following attributes:

            - ``device_id: str`` (required): The identifier of the mobile device
              that registers to push notification service.

            - ``object_status: ObjectStatus`` (required): THe current status of the
              registration of this device to push notification service.

            - ``registration_id: UUID`` (required): The identifier of the
              registration of the mobile device to the push notification service.

            - ``update_time: ISO8601DateTime`` (required): The time of the most
              recent modification of the properties of the mobile device's
              registration to the push notification service.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute('''
                INSERT INTO notification_device (
                    app_id,
                    account_id,
                    device_id,
                    device_platform,
                    device_token
                  )
                  VALUES (
                    %(app_id)s,
                    %(account_id)s,
                    %(device_id)s,
                    %(device_platform)s,
                    %(device_token)s
                  )
                  RETURNING
                    device_id,
                    object_status,
                    registration_id,
                    update_time
                ''',
                {
                    'account_id': account_id,
                    'app_id': app_id,
                    'device_id': device_id,
                    'device_platform': device_platform,
                    'device_token': device_token,
                }
            )

            row = cursor.fetch_one()
            device_registration = row.get_object({
                'object_status': ObjectStatus,
                'registration_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
            })

            return device_registration

    def __update_device_registration_token(
            self,
            registration_id: UUID,
            device_token: str,
            connection: RdbmsConnection = None
    ) -> Any:
        """
        Update the token of a device registered to the push notification
        service.


        :param registration_id: The identifier of the registration of a device
            to the push notification service.

        :param device_token: A token that identifies the device by the push
            notification provider of the device platform.

        :param connection: A connection to the notification database.


        :return: An object containing the following attributes:

            - ``device_id: str`` (required): The identifier of the mobile device
              that registers to push notification service.

            - ``object_status: ObjectStatus`` (required): The current status of the
              registration of this device to push notification service.

            - ``registration_id: UUID`` (required): The identifier of the
              registration of the mobile device to the push notification service.

            - ``update_time: ISO8601DateTime`` (required): The time of the most
              recent modification of information of the mobile device's registration
              to the push notification service.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            cursor = connection.execute(
                '''
                UPDATE 
                    notification_device
                  SET
                    device_token = %(device_token)s,
                    update_time = current_timestamp
                  WHERE
                    registration_id = %(registration_id)s
                  RETURNING
                    device_id,
                    object_status,
                    registration_id,
                    update_time
                ''',
                {
                    'registration_id': registration_id,
                    'device_token': device_token,
                }
            )

            row = cursor.fetch_one()
            device_registration = row.get_object({
                'object_status': ObjectStatus,
                'registration_id': cast.string_to_uuid,
                'update_time': cast.string_to_timestamp,
            })

            return device_registration

    def get_notification(self, notification_id: UUID) -> any:
        """
        Return the properties of the specified notification.


        :param notification_id: The identifier of a notification.


        :return: An object containing the following members:

            - ``creation_time: ISO8601DateTime`` (required): The time when the
              sender originated the notification to the intended recipient.

            - ``is_read: bool`` (required): Indicate whether the notification has
              been read by the intended recipient.

            - ``notification_id: UUID`` (required): The identifier of the
              notification.

            - ``notification_type: str`` (required): A string representation of the
              type of the notification, as selected by the sender that originated
              this notification to the intended recipient.

            - ``payload: json`` (optional): an arbitrary JSON expression added by
              the sender to provide information about the context of this
              notification.

            - ``schedule_time: ISO8601DateTime`` (required): THe time when this
              notification is scheduled to be sent to the intended recipient.  The
              notification is not visible to the intended recipient prior to this
              time.

            - ``sender_id: str`` (optional): The identifier of the sender that
              originated the notification.

            - ``update_time: ISO8601DateTime`` (required): The time of the most
              recent modification of an attribute of the notification, such as its
              read status.
        """
        with self.acquire_rdbms_connection() as connection:
            cursor = connection.execute(
                '''
                SELECT 
                    creation_time,
                    is_read,
                    notification_id,
                    notification_type,
                    payload,
                    schedule_time,
                    sender_id,
                    update_time
                  FROM
                    notification
                  WHERE
                    notification_id = %(notification_id)s
                ''',
                {
                    'notification_id': notification_id,
                }
            )

            row = cursor.fetch_one()
            if row is None:
                raise self.UndefinedObjectException(f'undefined notification "{notification_id}"')

            notification = row.get_object({
                'creation_time': cast.string_to_timestamp,
                'notification_id': cast.string_to_uuid,
                'payload': cast.string_to_json,
                'schedule_time': cast.string_to_timestamp,
                'update_time': cast.string_to_timestamp,
            })

            return notification

    def get_notifications(
            self,
            app_id: UUID,
            recipient_id: str,
            connection: RdbmsConnection = None,
            end_time: ISO8601DateTime = None,
            include_read: bool = False,
            limit: int = None,
            mark_read: bool = True,
            offset: int = None,
            notification_types: list[str] = None,
            sort_order: SortOrder = None,
            start_time: ISO8601DateTime = None) -> list[any]:
        """
        Return a list of notifications that have been sent to the specified
        recipient.


        :param app_id: The identifier of the client application that accesses
            the service.

        :param recipient_id: The identifier of a recipient that may have been
            issued notifications, such as, for instance the identification of
            a user account, or the identification of a device.

        :param connection: A connection to the notification database.

        :param end_time: The latest time of submission to return notifications.

        :param include_read: Indicate whether to include notifications that
            have been already read.

        :param limit: Constrain the number of notifications that are returned
            to the specified number.  Default value is
            ``NotificationService.DEFAULT_LIMIT``.  Maximum value is
            ``NotificationService.MAXIMUM_LIMIT``.

        :param mark_read: Indicate whether to mark as read every notification
            that are returned.

        :param notification_types: A list of notification types the recipient
            is interested in, or whatever notification if not defined.

        :param offset: Require to skip that many records before beginning to
            return notifications.  Default value is ``0``.  If both ``offset``
            and ``limit`` are specified, then ``offset`` records are skipped
            before starting to count the limit notifications that are
            returned.

        :param sort_order: The order to sort notifications by their schedule
            time.  Default to ``SortOrder.ascending``.

        :param start_time: The earliest time of submission to return
            notifications.


        :return: A list of objects containing the following members:

            - ``creation_time: ISO8601DateTime`` (required): The time when the
              sender originated the notification to the intended recipient.

            - ``is_read: bool`` (required): Indicate whether the notification has
              been read by the intended recipient.

            - ``notification_id: UUID`` (required): The identifier of the  notification.

            - ``notification_type: str`` (required): A string representation of the
              type of the notification, as selected by the sender that originated
              this notification to the intended recipient.

            - ``payload: json`` (optional): An arbitrary JSON expression added by
              the sender to provide information about the context of this
              notification.

            - ``schedule_time: ISO8601DateTime`` (required): The time when this
              notification is scheduled to be sent to the intended recipient.  The
              notification is not visible to the intended recipient prior to this
              time.

            - ``sender_id: str`` (optional): The identifier of the sender that
              originated the notification.

            - ``update_time: ISO8601DateTime`` (required): Time of the most recent
              modification of an attribute of the notification, such as its read
              status.
        """
        if sort_order is None:
            sort_order = SortOrder.ascending

        with self.acquire_rdbms_connection(auto_commit=mark_read, connection=connection) as connection:
            if mark_read:
                cursor = connection.execute(
                    f'''
                    UPDATE 
                        notification
                      SET
                        is_read = true
                      WHERE
                        notification_id IN (
                          SELECT 
                              notification_id
                            FROM
                              notification
                            WHERE
                              recipient_id = %(recipient_id)s
                              AND (%(start_time)s IS NULL OR creation_time > %(start_time)s)
                              AND (%(end_time)s IS NULL OR creation_time < %(end_time)s)
                              AND (%(include_read)s OR NOT is_read)
                              AND (%(notification_types)s IS NULL OR notification_type IN (%(notification_types)s))
                              AND object_status = %(OBJECT_STATUS_ENABLED)s
                            ORDER BY
                              creation_time {'ASC' if sort_order == SortOrder.ascending else 'DESC'}
                            OFFSET %(offset)s
                            LIMIT %(limit)s)
                      RETURNING 
                        notification_id,
                        notification_type,
                        is_read,
                        sender_id,
                        payload,
                        schedule_time,
                        creation_time,
                        update_time
                    ''',
                    {
                        'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                        'end_time': end_time,
                        'include_read': include_read,
                        'limit': min(limit or self.DEFAULT_LIMIT, self.MAXIMUM_LIMIT),
                        'notification_types': notification_types,
                        'offset': offset,
                        'recipient_id': recipient_id,
                        'start_time': start_time,
                    }
                )

            else:
                cursor = connection.execute(
                    f'''
                    SELECT 
                        notification_id,
                        notification_type,
                        is_read,
                        sender_id,
                        payload,
                        schedule_time,
                        creation_time,
                        update_time
                      FROM
                        notification
                      WHERE
                        recipient_id = %(recipient_id)s
                        AND (%(start_time)s IS NULL OR creation_time > %(start_time)s)
                        AND (%(end_time)s IS NULL OR creation_time < %(end_time)s)
                        AND (%(include_read)s OR NOT is_read)
                        AND (%(notification_types)s IS NULL OR notification_type IN (%(notification_types)s))
                        AND object_status = %(OBJECT_STATUS_ENABLED)s
                      ORDER BY
                        creation_time {'ASC' if sort_order == SortOrder.ascending else 'DESC'}
                      OFFSET %(offset)s
                      LIMIT %(limit)s
                    ''',
                    {
                        'OBJECT_STATUS_ENABLED': ObjectStatus.enabled,
                        'end_time': end_time,
                        'include_read': include_read,
                        'limit': min(limit or self.DEFAULT_LIMIT, self.MAXIMUM_LIMIT),
                        'notification_types': notification_types,
                        'offset': offset,
                        'recipient_id': recipient_id,
                        'start_time': start_time,
                    }
                )

            notifications = [
                row.get_object({
                    'creation_time': cast.string_to_timestamp,
                    'notification_id': cast.string_to_uuid,
                    'payload': cast.string_to_json,
                    'schedule_time': cast.string_to_timestamp,
                    'update_time': cast.string_to_timestamp,
                })
                for row in cursor.fetch_all()
            ]

            return notifications

    def register_device(
            self,
            app_id: UUID,
            device_id: str,
            device_token: str,
            device_platform: DevicePlatform,
            account_id: UUID = None,
            connection: RdbmsConnection = None,
            topics: list[str] = None
    ) -> any:
        """
        Register a device to receive push notification messages from the
        platform.


        :note: The function registers the device on behalf of the application
            identification of the server platform, not the identification of
            the client application itself.  An instance of a server platform
            is specific to a particular service to which client applications,
            whatever their platform (Android, iOS, Web, etc.) and therefore
            whatever their application identification, are interested in
            receiving push notifications.


        :todo: The argument "topics" is not used at the moment.


        :param app_id: The identifier of the client application that accesses
            the service.

        :param device_id: The identifier of the device, which depends on the
            device platform:

            - Android: On Android 8.0 (API level 26) and higher versions of the
              platform, a 64-bit number (expressed as a hexadecimal string), unique
              to each combination of app-signing key, user, and device.  The value
              may change if a factory reset is performed on the device or if an
              APK signing key changes.

            - iOS: The unique identifier of the iOS device, previously the
              Unique Device Identifier (UDID) of the device, which is a
              40-character string that is tied to this specific Apple device.
              It could be a SecureUDID, which is an open-source sandboxed UDID
              solution aimed at solving the main privacy issues that caused
              Apple to deprecate UDIDs.

        :param device_token: A token that identifies the device by the push
            notification provider of the device platform.

            - Android: A token identifying the device to push the notification to,
              i.e., the registration ID.  A device token is an opaque identifier
              of a device that Android Google Cloud Messaging (GCM) gives to the
              device when it first connects with it.  The device shares the device
              token with its provider.  The device token is analogous to a phone
              number; it contains information that enables GCM to locate the device
              on which the client application is installed.  GCM also uses it to
              authenticate the routing of a notification.

            - iOS: A token identifying the iOS device to push the notification to.
              A device token is an opaque identifier of a device that APNs gives to
              the device when it first connects with it.  The device shares the
              device token with its provider. Thereafter, this token accompanies
              each notification from the provider.  The device token is analogous
              to a phone number; it contains information that enables APNs to locate
              the device on which the client application is installed. APNs also
              uses it to authenticate the routing of a notification.  A device token
              is not the same thing as the device UDID returned by the
              ``uniqueIdentifier`` property of ``UIDevice``.

        :param device_platform: The platform of the end user's mobile device:

            - `ios`: Apple iOS

            - `android`: Google Android

            - `windows`: Windows Phone

        :param account_id: The identifier of the account of the user on behalf
            of whom the device is registered to receive push notification
            messages.

        :param connection: A connection to the notification database.

        :param topics: A list of keywords representing topics the end user is
            interested in to be pushed new content whenever related to one of
            those topics.  The list of supported keywords is specific to the
            publisher service of the client application and as such the
            developer of the client application has to refer to the technical
            documentation of the publisher service.


        :return: An object containing the following attributes:

            - ``device_id: str`` (required): The identifier of the mobile device
              that registers to push notification service.

            - ``object_status: ObjectStatus` (required): The current status of the
              registration of this device to push notification service.

            - ``registration_id: UUID`` (required): The identifier of the
              registration of the mobile device to the push notification service.

            - ``update_time: ISO8601DateTime`` (required): The time of the most
              recent modification of properties of the mobile device's registration
              to the push notification service.
        """
        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            ApplicationService().get_application_with_id(app_id, check_status=True, connection=connection)

            device_registration = self.__get_device_registration(
                device_id,
                app_id,
                account_id=account_id,
                connection=connection
            )

            if device_registration is None:
                device_registration = self.__register_device(
                    device_id,
                    device_platform,
                    app_id,
                    device_token,
                    account_id=account_id,
                    connection=connection
                )
            elif device_registration.device_token != device_token:
                device_registration = self.__update_device_registration_token(
                    device_registration.registration_id,
                    device_token,
                    connection=connection
                )

            return device_registration

    def send_notification_v2(
            self,
            app_id: UUID,
            notification: Notification,
            connection: RdbmsConnection = None,
            if_not_exists: bool = False,
            lifespan: int = DEFAULT_LIFESPAN,
            notification_mode: NotificationMode = None,
            schedule_time: ISO8601DateTime = None,
            sender_id: str = None
    ) -> Any:
        recipient_ids = notification.recipient_ids
        if not recipient_ids:
            raise ValueError('No recipients specified')

        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            # Remove any recipients who would have already received a similar
            # notification.
            if if_not_exists:
                already_notified_recipient_ids = self.__filter_already_notified_recipients(
                    notification.notification_type,
                    recipient_ids,
                    connection=connection,
                    sender_id=sender_id
                )

                recipient_ids = list(set(recipient_ids) - set(already_notified_recipient_ids))
                if len(recipient_ids) == 0:
                    return

            # Determine the expiration time of this notification.
            expiration_time = ISO8601DateTime.now() + datetime.timedelta(
                seconds=max(lifespan or self.DEFAULT_LIFESPAN, self.MAXIMUM_LIFESPAN))

            # Register this notification for every recipient.
            logging.debug(notification.payload.__dict__)

            cursor = connection.execute(
                '''
                INSERT INTO notification (
                    app_id,
                    content_title,
                    content_text,
                    expiration_time,
                    notification_mode,
                    notification_type,
                    payload,
                    recipient_id,
                    schedule_time,
                    sender_id
                  )
                  VALUES
                    %[values]s
                  RETURNING
                    notification_id,
                    recipient_id
                ''',
                {
                    'values': [
                        (
                            app_id,
                            notification.content_title,
                            notification.content_text,
                            expiration_time,
                            notification_mode or NotificationMode.push,
                            notification.notification_type,
                            notification.payload and json.dumps(obj.stringify(notification.payload, trimmable=True)),
                            recipient_id,
                            schedule_time,
                            sender_id,
                        )
                        for recipient_id in recipient_ids
                    ]
                }
            )

            notifications = [
                row.get_object({
                    'notification_id': cast.string_to_uuid,
                })
                for row in cursor.fetch_all()
            ]

            return notifications

    def send_notification(
            self,
            app_id: UUID,
            notification_type: str,
            connection: RdbmsConnection = None,
            content_title: str = None,
            content_text: str = None,
            recipient_ids: str or list[str] = None,
            if_not_exists: bool = False,
            lifespan: int = DEFAULT_LIFESPAN,
            notification_mode: NotificationMode = None,
            # package_name: str = None,
            payload: json = None,
            sender_id: str = None,
            schedule_time: ISO8601DateTime = None,
            recipient_timezones: dict[str, int] = None) -> Any:
        """
        Send a notification to the intended recipient(s) as soon as possible
        or at a given time.

        The notification and its content is stored for later delivery up to a
        maximum period of time, the lifespan of the notification, also known
        as its time-to-live(TTL).  The primary reason for this is that a
        device may be unavailable (e.g., turned off, no network coverage).


        :param app_id: The identifier of the client application that accesses
            the service.

        :param notification_type: The type of the notification to be sent, such
            as for instance `on_something_happened`.

        :param connection: A connection to the notification database.

        :param content_title: The title (first row) of the notification, in a
            standard notification.  It corresponds to the localized text that
            provides the notification’s primary description.

        :param content_text: The text (second row) of the notification, in a
            standard notification.  It corresponds to the localized text that
            provides the notification’s main content.

        :param recipient_ids: The identifier of a recipient, or a list of
            identifiers of recipients, to send the notification to.

        :param if_not_exists: Indicate whether the notification needs to be
            ignored for a particular recipient if the latter already received
            a notification of the same type that the recipient has not yet
            read.  The function doesn't check whether a previous notification
            of the same type may have a different payload.

        :param lifespan: The period of time expressed in seconds during which
            information of the notification reasonably may be expected
            usefully to inform an action or interest of the intended
            recipients.  After the lifespan expires, provision of the
            notification to the recipients may be prevented; the notification
            and its content may be deleted.  The maximum lifespan is
            ``NotificationService.MAXIMUM_LIFESPAN``.

        :param notification_mode: The mode to deliver this notification to the
            recipients.

        :param payload: Any arbitrary JSON expression added by the sender to
            provide information about the context of this notification.

        :param sender_id: The identifier of the sender on behalf whom the
            notification is sent to the recipients.

        :param schedule_time: The time when this notification needs to be sent
            to the intended recipient.  The notification is not visible to the
            intended recipient prior to this time.  If not specified, the
            notification is sent as soon as possible.

        :param recipient_timezones: A dictionary of time zones of the intended
            recipients for which the schedule time is expected to be in their
            local time.  The key corresponds to the identifier of an intended
            recipient, and the value corresponds to time zone of this
            particular recipient.

            When a time zone is defined for a particular recipient, the
            function understands that the schedule time of the notification
            for this recipient has to be converted to the local time of this
            recipient.  The function converts ``schedule_time`` to UTC, and it
            strips the time zone information to get a local time to which the
            function adds the recipient's time zone.

            For instance, if the specified schedule time is
            ``2013-12-20 15:00:00+07`` and the time zone ``+7`` is specified
            for a recipient, the schedule time is assumed to be the local time
            ``2013-12-20 08:00:00`` for the region, i.e., time zone, of this
            recipient.  The resulting schedule time with time zone for this
            recipient is then ``2013-12-20 08:00:00+07``


        :return: A list of objects containing the following attributes:

            - ``notification_id: UUID`` (required): The identifier of the
              notification sent to a particular recipient.

            - ``recipient_id: str``: The string representation of the identification
              of the recipient intended to be delivered this notification.
        """
        if not recipient_ids:
            return

        if not isinstance(recipient_ids, (list, set, tuple)):
            recipient_ids = [recipient_ids]

        # Remove any duplicated recipient identifiers.
        recipient_ids = list(set([
            str(recipient_id)
            for recipient_id in recipient_ids
        ]))

        with self.acquire_rdbms_connection(auto_commit=True, connection=connection) as connection:
            # Remove any recipients who would have already received a similar
            # notification.
            if if_not_exists:
                already_notified_recipient_ids = self.__filter_already_notified_recipients(
                    notification_type,
                    recipient_ids,
                    connection=connection,
                    sender_id=sender_id
                )

                recipient_ids = list(set(recipient_ids) - set(already_notified_recipient_ids))

                if len(recipient_ids) == 0:
                    return

            # Determine the expiration time of this notification.
            expiration_time = ISO8601DateTime.now() + datetime.timedelta(
                seconds=max(lifespan or self.DEFAULT_LIFESPAN, self.MAXIMUM_LIFESPAN))

            # Register this notification for every recipient.
            cursor = connection.execute(
                '''
                INSERT INTO notification (
                    app_id,
                    content_title,
                    content_text,
                    expiration_time,
                    notification_mode,
                    notification_type,
                    payload,
                    recipient_id,
                    schedule_time,
                    sender_id
                  )
                  VALUES
                    %[values]s
                  RETURNING
                    notification_id,
                    recipient_id
                ''',
                {
                    'values': [
                        (
                            app_id,
                            content_title,
                            content_text,
                            expiration_time,
                            notification_mode or NotificationMode.push,
                            notification_type,
                            payload and json.dumps(obj.stringify(payload, trimmable=True)),
                            recipient_id,
                            schedule_time,
                            sender_id,
                        )
                        for recipient_id in recipient_ids
                    ]
                }
            )

            notifications = [
                row.get_object({
                    'notification_id': cast.string_to_uuid,
                })
                for row in cursor.fetch_all()
            ]

            return notifications

    def unregister_device(
            self,
            app_id: UUID,
            device_id: str,
            account_id: UUID = None) -> None:
        """
        Unregister a device from receiving push notification messages.


        :param app_id: The identifier of the client application that accesses
            the service.

        :param device_id: The device's identifier, which depends on the device
            platform:

            - Android: On Android 8.0 (API level 26) and higher versions of the
              platform, a 64-bit number (expressed as a hexadecimal string), unique
              to each combination of app-signing key, user, and device.  The value
              may change if a factory reset is performed on the device or if an
              APK signing key changes.

            - iOS: unique identifier of the iOS device, previously the
              Unique Device Identifier (UDID) of the device, which is a
              40-character string that is tied to this specific Apple device.
              It could be a SecureUDID, which is an open-source sandboxed UDID
              solution aimed at solving the main privacy issues that caused
              Apple to deprecate UDIDs.

        :param account_id: The identifier of the account of the user on behalf
            of whom the device is unregistered from receiving push
            notification messages.
        """
        with self.acquire_rdbms_connection(True) as connection:
            connection.execute(
                '''
                DELETE FROM 
                    notification_device
                  WHERE 
                    device_id = %(device_id)s
                    AND (
                      (account_id IS NULL AND %(account_id)s IS NULL) 
                      OR account_id = %(account_id)s
                    )
                    AND app_id = %(app_id)s
                ''',
                {
                    'account_id': account_id,
                    'app_id': app_id,
                    'device_id': device_id,
                }
            )








# def flush_notifications(self, app_id, account_id,
#         service_name=None, notification_types=None):
#     """
#     Flush all the notifications originated from the given client
#     application that were sent to the specified user.
#
#     :param app_id: identification of the client application such as a Web,
#         a desktop, or a mobile application, that accesses the service.
#     :param account_id: identification of the account of the user to flush
#         all the notifications he receives from the given application.
#     :param service_name: code name of the service that originated the
#         notifications to flush.  By convention, the code name of the
#         service corresponds to the Python class of this service (cf.
#         `self.__class__.__name__`).
#     :param notification_types: a list of types of the notifications to
#         flush.  If no list is provided, the function flushes all the
#         notifications that the client application posted to the user.
#     """
#     with self.acquire_rdbms_connection(True) as connection:
#         if notification_types is None:
#             connection.execute("""
#                 DELETE FROM notification
#                   WHERE recipient_id = %(account_id)s
#                     AND app_id = %(app_id)s
#                     AND object_status = %(OBJECT_STATUS_ENABLED)s
#                     AND (%(service_name) IS NULL OR service_name = %(service_name)s)""",
#                 { 'OBJECT_STATUS_DISABLED': OBJECT_STATUS_DISABLED,
#                   'OBJECT_STATUS_ENABLED': OBJECT_STATUS_ENABLED,
#                   'app_id': app_id,
#                   'recipient_id': account_id,
#                   'service_name': service_name })
#         else:
#             connection.execute("""
#                 DELETE FROM notification
#                   WHERE recipient_id = %(account_id)s
#                     AND app_id = %(app_id)s
#                     AND object_status = %(OBJECT_STATUS_ENABLED)s
#                     AND (%(service_name) IS NULL OR service_name = %(service_name)s)
#                     AND notification_type IN (%[notification_types]s)""",
#                 { 'OBJECT_STATUS_DISABLED': OBJECT_STATUS_DISABLED,
#                   'OBJECT_STATUS_ENABLED': OBJECT_STATUS_ENABLED,
#                   'app_id': app_id,
#                   'notification_types': notification_types,
#                   'recipient_id': account_id,
#                   'service_name': service_name })

# def mark_notifications(self, app_id, account_id, notification_ids,
#         mark_read=True):
#     """
#     Update the read mark of a list of notifications sent to the specified
#     user.
#
#     :param app_id: identification of the client application such as a Web,
#            a desktop, or a mobile application, that accesses the service.
#
#     :param account_id: identification of the account of a user whom the
#            specified notifications have been sent to.
#
#     :param notification_ids: a list of notification to mark as read or
#            unread.
#
#     :param mark_read: indicate whether to mark as read the specified
#         notifications.
#     """
#     if notification_ids is None:
#         return
#
#     if type(notification_ids) not in (list, set, tuple):
#         notification_ids = [ notification_ids ]
#
#     if len(notification_ids) == 0:
#         return
#
#     with self.acquire_rdbms_connection(True) as connection:
#         cursor = connection.execute("""
#             UPDATE notification
#               SET is_read = %(mark_read)s,
#                   update_time = current_timestamp
#               WHERE notification_id IN (%[notification_ids]s)
#                 AND recipient_id = %(account_id)s
#                 AND is_read <> %(mark_read)s
#               RETURNING notification_id""",
#             { 'account_id': account_id,
#               'mark_read': mark_read,
#               'notification_ids': notification_ids })
#         missing_notification_ids = set(notification_ids) \
#             - set([ row.get_value('notification_id', cast.string_to_uuid) for row in cursor.fetch_all() ])
#         if len(notification_ids) > 0:
#             raise self.UndefinedObjectException('Some specified notifications have not been sent to this user or their state do not change',
#                 payload=missing_notification_ids)


#
#     def _post_notification(self, app_id, notification_type,
#             notification_mode=NotificationMode.pull,
#             account_ids=None, device_ids=None,
#             payload=None, lifespan=None,
#             topics=None,
#             schedule_time=None, use_local_time=False,
#             is_broadcast=False, is_unique=False, is_volatile=False, is_product_based=False):
#         """
#
#
# The function checks whether the  payload, if any provided, is of a
# simple type such as a number (integer, decimal, complex) or a string.
# If not, the function convert the payload to a string representation
# of a JSON expression.
#
# :warning: this function is for internal usage only; it MUST not be
#     surfaced to any client applications through a RESTful API.
#
# :param app_id: identification of the client application such as a Web,
#     a desktop, or a mobile application, that accesses the service.
# :param notification_type: type of the notification such as
#     `on_something_happened`.
# :param notification_mode:
#
# :param account_ids: list of account identifications of users to send
#     the notification to.
# :param device_ids: list of identifications of devices to send the
#     notification to.
#
# :param payload: content of the notification to send to the recipients.
#     The content could be a simple string caption, or an object which
#     the function converts its JSON expression.into a string
#     representation.
# :param lifespan: duration in minutes the notification lives before it
#     is deleted.  If not defined, the notification persists forever as
#     long as it is not read.
# :param topics: a list of keywords indicating the subjects of this
#     notifications.  Only the subscribers who have registered for these
#     topics will be pushed this notification.
#
# :param schedule_time: schedule the notification to automatically be
#     sent later at the given time.  If not specified, the notification
#     is sent as soon as possible.
# :param use_local_time: indicate whether the schedule time is assumed
#     to be in local time of a particular device.  If so, the
#     `schedule_time` is converted to UTC, and the time zone
#     information is then stripped out to provide a local time.  For
#     instance, if the specified schedule time is `2013-12-20 13:00:00+07`
#     and the argument `use_local_time` is set to `True`, the
#     schedule time is assumed to be the local time `2013-12-20 06:00:00`
#     for the region, i.e., time zone, of a particular device to send
#     the notification to.
#
# :param is_broadcast: indicate whether the notification needs to be
#     sent to every user who subscribed for receiving notification from
#     this application (determined by `app_id`), or more generally
#     from the product this application belongs to (if the argument
#     `is_product_based` is `True`).
#         """
#
#         if account_ids is None and device_ids is None:
#             raise self.InvalidArgumentException('No recipient has been specified')
#
#         if schedule_time and expiration_time and schedule_time > expiration_time:
#             raise self.InvalidArgumentException('The expiration time of a message MUST be posterior to the specified schedule time')
#
#         # If the payload of the message is not a simple type, convert it to a
#         # string representation of a JSON expression.
#         #
#         # :note: `basestring` includes `str` and `unicode`.
#         if payload and not isinstance(payload,  (basestring, int, long, float, complex)):
#             payload = obj.jsonify(payload)


# def send_device_notification(self, app_id, notification_type, device_ids,
#         notification_mode=NotificationMode.push,
#         if_not_exists=False,
#         lifespan=DEFAULT_LIFESPAN,
#         payload=None,
#         sender_id=None):
#     """
#     Send a notification to the intended device(s) as soon as possible or
#     at a given time.
#
#     The notification and its content is stored for later delivery up to a
#     maximum period of time, the lifespan of the notification, also known
#     as its time-to-live(TTL).  The primary reason for this is that a
#     device may be unavailable (e.g., turned off, no network coverage).
#
#
#     :param app_id: identification of the client application such as a Web,
#         a desktop, or a mobile application, that accesses the service.
#
#     :param notification_type: type of the notification to be sent, such as
#         for instance `on_something_happened`.
#
#     :param device_ids: identification of the device, or a list of
#         identifications of devices, to send the notification to.
#
#     :param if_not_exists: indicate whether the notification needs to be
#         ignored for a particular device if the latter already received a
#         notification of the same type that the device has not yet read.
#         The function doesn't check whether a previous notification of the
#         same type may have a different payload.
#
#     :param lifespan: period of time expressed in seconds during which
#         information of the notification reasonably may be expected
#         usefully to inform an action or interest of the intended devices.
#         After the lifespan expires, provision of the notification to the
#         devices may be prevented; the notification and its content may be
#         deleted.  The maximum lifespan is `NotificationService.MAXIMUM_LIFESPAN`.
#
#     :param payload: any arbitrary JSON expression added by the sender to
#         provide information about the context of this notification.
#
#     :param sender_id: identification of the sender on behalf whom the
#         notification is sent to the devices.
#
#
#     :return: a list of instances containing the following members:
#
#         - `creation_time` (required): time when the notification was
#           registered to the platform.
#
#         - `device_id` (required): identification of a device that is sent
#           this notification.
#
#         - `notification_id` (required): identification of the notification
#           sent to the device.
#     """
#     if device_ids is None:
#         return
#
#     if not isinstance(device_ids, (list, set, tuple)):
#         device_ids = [ device_ids ]
#
#     with self.acquire_rdbms_connection(True) as connection:
#         # Filter out from the list of the devices to send this notification
#         # those that have received this notification type but not read yet.
#         if if_not_exists == True:
#             cursor = connection.execute("""
#                 SELECT DISTINCT device_id
#                   FROM notification2device
#                   WHERE device_ud IN (%[device_ids]s)
#                     AND (%(account_id)s IS NULL OR account_id = %(account_id)s)
#                     AND notification_type = %(notification_type)s
#                     AND is_unread
#                     AND (expiration_time IS NULL OR expiration_time > current_timestamp)""",
#                 { 'notification_type': notification_type,
#                   'device_ids': device_ids,
#                   'account_id': sender_id })
#             device_ids = set(device_ids) - set([ row.get_value('device_id') for row in cursor.fetch_all() ])
#             if len(device_ids) == 0:
#                 return
#
#         cursor = connection.execute("""
#             INSERT INTO notification2device(
#                   notification_type,
#                   notification_mode,
#                   device_id,
#                   sender_id,
#                   payload,
#                   expiration_time,
#                   app_id)
#               VALUES %[values]s
#               RETURNING notification_id,
#                         device_id,
#                         creation_time""",
#             { 'values': [ (notification_type,
#                            notification_mode,
#                            device_id,
#                            sender_id,
#                            payload and obj.jsonify(payload),
#                            lifespan and (True, "current_timestamp + '%d seconds'::interval" % lifespan),
#                            app_id)
#                     for device_id in device_ids ] })
#
#         return [ row.get_object({
#                         'creation_time': cast.string_to_timestamp,
#                         'notification_id': cast.string_to_uuid })
#                 for row in cursor.fetch_all() ]


# def send_notifications(self, app_id, notification_type, recipient_ids, payloads,
#         if_not_exists=False,
#         lifespan=DEFAULT_LIFESPAN,
#         notification_mode=NotificationMode.pull,
#         package_name=None,
#         sender_id=None,
#         schedule_time=None,
#         recipient_timezones=None):
#
#     if not recipient_ids:
#         return
#
#     recipient_ids = [ str(recipient_ids) ] if not isinstance(recipient_ids, (list, set, tuple)) \
#             else [ str(recipient_id) for recipient_id in recipient_ids ]
#
#     json_payloads = [ obj.jsonify(payload) for payload in payloads ]
#
#     with self.acquire_rdbms_connection(True) as connection:
#         if if_not_exists:
#             cursor = connection.execute("""
#                 SELECT DISTINCT recipient_id
#                   FROM notification
#                   WHERE notification_type = %(notification_type)s
#                     AND recipient_id IN (%[recipient_ids]s)
#                     AND (%(sender_id)s IS NULL OR sender_id = %(sender_id)s)
#                     AND NOT is_read""",
#                 { 'notification_type': notification_type,
#                   'recipient_ids': recipient_ids,
#                   'sender_id': sender_id })
#
#             recipient_ids = set(recipient_ids) - set([ row.get_value('recipient_id') for row in cursor.fetch_all() ])
#
#             if len(recipient_ids) == 0:
#                 return
#
#         cursor = connection.execute("""
#             INSERT INTO notification(
#                 notification_type,
#                 notification_mode,
#                 recipient_id,
#                 sender_id,
#                 payload,
#                 schedule_time,
#                 expiration_time,
#                 app_id,
#                 package_name)
#               VALUES %[values]s
#               RETURNING notification_id,
#                         recipient_id""",
#             { 'values': [
#                     (notification_type,
#                      notification_mode,
#                      recipient_id,
#                      sender_id,
#                      json_payload,
#                      (True, 'DEFAULT') if schedule_time is None \
#                         else schedule_time if (recipient_timezones is None or recipient_timezones.get(recipient_id) is None) \
#                         else cast.string_to_timestamp('%s%+03d' % (str(schedule_time)[:-6] ), recipient_timezones[recipient_id]),
#                      (True, "current_timestamp + '%d seconds'::interval" % max(lifespan, self.MAXIMUM_LIFESPAN)),
#                      app_id,
#                      package_name)
#                     for json_payload in json_payloads
#                         for recipient_id in recipient_ids ] })
#
#         return [ row.get_object({ 'notification_id': cast.string_to_uuid })
#                 for row in cursor.fetch_all() ]

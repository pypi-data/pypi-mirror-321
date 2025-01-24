# Perseus: RESTful API Server Framework

Perseus is a Python framework for quickly building RESTful API servers with minimal effort.

Perseus provides an initial set of core services that supports the following features:

- Client application registration with API keys generation
- Client application access control with RESTful request signature
- Client application and RESTful API server version compatibility check
- User authentication and session management
- Team/group management
- RESTful request logging with data sensitiveness support
- RESTful service automatic discovery
- HTTP request query parameters & body JSON message automatically parsing (depending on the HTTP method used) with data type check and conversion

Perseus is based on [Tornado](https://www.tornadoweb.org/) for handling client network connection.

## RESTful API Request Handler

```python
from majormode.perseus.service.base_http_handler import HttpRequest
from majormode.perseus.service.base_http_handler import HttpRequestHandler
from majormode.perseus.service.base_http_handler import http_request

import AttendantService


class AttendantServiceHttpRequestHandler(HttpRequestHandler):
    @http_request(r'^/attendant/session$',
                  http_method=HttpRequest.HttpMethod.POST,
                  authentication_required=False,
                  sensitive_data=True,
                  signature_required=False)
    def sign_in(self, request):
        email_address = request.get_argument(
            'email_address',
            data_type=HttpRequest.ArgumentDataType.email_address,
            is_required=True)

        password = request.get_argument(
            'password',
            data_type=HttpRequest.ArgumentDataType.string,
            is_required=True)

        return AttendantService().sign_in(request.app_id, email_address, password)
```

## Configure the environment variables

```env
# Copyright (C) 2021 Majormode.  All rights reserved.
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

# Connection properties of the RESTful API server instances.  Defaults
# to 127.0.0.1:8081.
API_SERVER_HOSTNAME=127.0.0.1
API_SERVER_PORTS=

# Root path of the Network File System (NFS) -- referring to the
# distributed file system (not the protocol) -- where the Content
# Delivery Network (CDN) files are stored into, such as avatars, etc.
CDN_NFS_ROOT_PATH=

# Hostname of the Content Delivery Network (CDN) server that hosts media
# files such as avatars, etc.
CDN_URL_HOSTNAME=

# Environment stage of the API server instances.  Possible values are:
#
# - dev
# - int
# - staging
# - prod
#
# Defaults to `dev`.
ENVIRONMENT_STAGE=

# Connection properties to a Memcached server (a distributed memory
# object caching system).  Defaults to 127.0.0.1:11211.
MEMCACHED_HOSTNAME = '127.0.0.1'
MEMCACHED_PORT = 11211

# Threshold for the logger to level.  Logging messages which are less
# severe than the specified level will be ignored; logging messages
# which have this severity level or higher will be emitted.  Possible
# values are:
#
# - debug
# - info
# - warning
# - error
# - critical
#
# Default to 'debug'.
LOGGING_LEVEL=

# Environment variables to select default parameter values to connect
# to PostgreSQL Relational Database Management System.
PG_HOSTNAME=localhost
PG_PORT=5432
PG_DATABASE_NAME=
PG_USERNAME=
PG_PASSWORD=
```

## Run the RESTful API Server Processes

```bash
$ fab start --port=65180,65181,...
```

Hashtags/Topics: `#perseus` `#restful` `#api` `#server` `#framework` `#python`

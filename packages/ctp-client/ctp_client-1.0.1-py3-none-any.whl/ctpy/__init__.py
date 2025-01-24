# Copyright 2017 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import Optional

from .import version
from .client import CTPYclient

__version__ = version.version


def connect(host: str,
            port: int,
            username: str,
            password: str,
            rate_limit: Optional[int] = None) -> CTPYclient:
    """
    Createa a connection to a CTP server

    :param host: host to connect to
    :param port: port to connect to
    :param username: username to login as
    :param password: password for user
    :param rate_limit: optionally limit the time between requests, this is specified
                       as the maximum requests per second

    :return: CTP client object
    """
    ctpy_client = CTPYclient(host, port, username, password, rate_limit)
    return ctpy_client

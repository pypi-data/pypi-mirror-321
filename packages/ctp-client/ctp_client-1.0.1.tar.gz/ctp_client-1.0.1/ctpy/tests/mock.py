# Copyright 2024 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Pattern, Union

from requests import Response
from requests_mock import Mocker


class CTPRequestsMocker(Mocker):
    uri: str = "http://ctp.example.com"
    port: int = 1080

    def request(self,
                method: str,
                url: Union[str, Pattern[str]],
                **kwargs: Any) -> Response:
        url = f"{self.uri}:{self.port}/{url.lstrip('/')}"
        print(f'Mocking request for {url}')
        return super().request(method, url, **kwargs)

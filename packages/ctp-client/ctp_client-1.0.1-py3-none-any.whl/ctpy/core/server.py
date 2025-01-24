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


import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

from ctpy import exceptions
from ctpy.core import Pipeline


class CTPServer():
    def __init__(self, ctpy_session):
        self.ctpy_session = ctpy_session
        response = self.ctpy_session.get('server')
        if response.status_code != 200:
            raise exceptions.CTPYServerXMLParseError()
        xml_string = response.text
        try:
            server = ET.fromstring(xml_string)
        except ParseError as exc:
            raise exceptions.CTPYServerXMLParseError(exc)

        # {'build': '2021.04.01 at 11:04:40 CDT', 'ip': '10.42.0.83', 'java': '1.7', 'port': '1080'}
        self.build = server.attrib['build']
        self.ip = server.attrib['ip']
        self.java = server.attrib['java']
        self.port = server.attrib['port']
        self.pipelines = {}

        for configuration in server:
            if configuration.tag != 'Configuration':
                raise exceptions.CTPYServerXMLParseError
            pipeline_id = 0
            for child in configuration:
                if child.tag == 'Pipeline':
                    self.pipelines[child.attrib['name']] = Pipeline(self, pipeline_id, child)
                    pipeline_id += 1

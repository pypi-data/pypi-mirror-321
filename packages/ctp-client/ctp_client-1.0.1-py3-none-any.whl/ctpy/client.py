# Copyright 2022 Biomedical Imaging Group Rotterdam, Department of
# Radiology, Erasmus MC, Rotterdam, The Netherlands

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import re
from time import time, sleep
from typing import Dict, List, Optional

import requests
from requests.exceptions import ConnectionError as RequestsConnectionError

from ctpy import exceptions
from ctpy.core import CTPServer
from ctpy.core.stages import ObjectTracker
from ctpy.helpers import parse_idmap_results, parse_object_tracker_results, parse_summary, parse_step, CtpSummary


class CTPYclient():

    def __init__(self, host: str, port: int, username: str, password: str, rate_limit: Optional[int] = None):
        self.host: str = host
        self.port: int = port
        self.headers: Dict[str, str] = {}

        if username is None:
            logging.debug(f'No username information')
            self.session: requests.Session = requests.Session()
        else:
            logging.debug(f'Log in as user: {username}')
            self.session: requests.Session = self._login(username, password)

        self.rate_limit: int = rate_limit
        self.server: CTPServer = CTPServer(self)

    def _login(self, username: str, password: str) -> requests.Session:
        cookies = {
            'CTP': 'session',
        }

        headers = {
            'Connection': 'keep-alive',
            'Referer': f'{self.host}:{self.port}/',
        }

        timestamp = int(time())
        query = f'username={username}&password={password}&url=/&timestamp={timestamp}'
        login_uri = f'{self.host}:{self.port}/login?{query}'
        logging.debug(f'Logging in using url: {login_uri}')
        try:
            response = requests.get(login_uri, cookies=cookies,
                                    headers=headers, allow_redirects=False)
            logging.debug(f'got response: {response}')
        except RequestsConnectionError as esc:
            raise exceptions.CTPYLoginException(esc)

        if response.status_code == 302 and 'RSNASESSION' in response.cookies:
            logging.debug('Succesfully connected to CTP')
            session = requests.Session()
            session.cookies.update({
                'RSNASESSION': response.cookies['RSNASESSION']
            })
        else:
            raise exceptions.CTPYLoginException
        return session

    def _rate_limit(self):
        if self.rate_limit:
            sleep(1 / self.rate_limit)

    def format_uri(self, path: str, query: Optional[str] = None) -> str:
        if path and path[0] != '/':
            path = '/' + path
        if query and query[0] != '?':
            query = '?' + query

        if not query:
            query = ''
        if not path:
            path = ''

        return f'{self.host}:{self.port}{path}{query}'

    def get(self,
            path: str,
            query: Optional[str] = None,
            timeout: Optional[float] = None,
            headers: Dict[str, str] = None) -> requests.Response:
        """
        Process a REST GET to the server

        :param path: path for the request
        :param query: query string to use for the request
        :param timeout: timeout
        :param headers: request headers
        :return: requests response
        """
        uri = self.format_uri(path, query)
        logging.debug('GET: %s', uri)
        self._rate_limit()
        try:
            response = self.session.get(uri, timeout=timeout, headers=headers)
        except RequestsConnectionError as esc:
            raise exceptions.CTPYConnectionAborted(esc)
        return response

    def put(self,
            path: str,
            query: Optional[str] = None,
            timeout: Optional[float] = None,
            headers: Dict[str, str] = None) -> requests.Response:
        uri = self.format_uri(path, query)
        logging.debug('PUT: %s', uri)
        self._rate_limit()
        try:
            response = self.session.put(uri, timeout=timeout, headers=headers)
        except RequestsConnectionError as esc:
            raise exceptions.CTPYConnectionAborted(esc)
        return response

    def post(self,
             path: str,
             data,
             query: Optional[str] = None,
             timeout: Optional[float] = None,
             headers: Dict[str, str] = None) -> requests.Response:
        uri = self.format_uri(path, query)
        logging.debug('POST: %s', uri)
        self._rate_limit()
        try:
            response = self.session.post(uri, data=data, timeout=timeout, headers=headers)
        except RequestsConnectionError as esc:
            raise exceptions.CTPYConnectionAborted(esc)
        return response

    def get_ctp_summary(self) -> List[CtpSummary]:
        response = self.get('/summary?suppress')
        if response.status_code == 200:
            logging.debug('Succesfully got html')
        elif response.status_code == 403:
            logging.error('Forbidden')
            raise exceptions.CTPYAccessException
        else:
            raise exceptions.CTPYGeneralError

        results = parse_summary(response.content)
        return results

    def get_ctp_step(self, pipeline: int, step: int) -> Dict[str, Dict[str, str]]:
        response = self.get(f'/summary?p={pipeline}&s={step}&suppress')
        print(f"{response.status_code}=")

        if response.status_code == 200:
            logging.debug('Succesfully got html')
        elif response.status_code == 403:
            logging.error('Forbidden')
            raise exceptions.CTPYAccessException
        else:
            raise exceptions.CTPYGeneralError

        if "<title>ERROR</title>" in response.text:
            match = re.search("java.lang.IndexOutOfBoundsException: Index (\d+) out of bounds for length (\d+)", response.text)

            if match:
                index = match.group(1)
                length = match.group(2)

                raise IndexError(f"Index out of range {index=} {length=}")
            else:
                raise exceptions.CTPYGeneralError

        results = parse_step(response.content)
        return results

    def add_to_lookup(self, stage_id, key, value):
        query = f'id={stage_id}&key={key}&value={value}'
        response = self.put('/lookup', query)
        if response.status_code == 200:
            logging.info('Succesfully added Key/Value')
        elif response.status_code == 304:
            logging.warning('Did not modified key/value')
            raise exceptions.CTPYFailedAddingLUT
        elif response.status_code == 403:
            logging.error('Forbidden')
            raise exceptions.CTPYAccessException
        else:
            raise exceptions.CTPYGeneralError
        # logging.debug(response.content)

    def get_object_tracker_patient_info(self, pipeline_id, stage_id, key='', patient_id=None, study_uid_filter=None):
        # headers = self.headers.copy()
        headers = {}
        headers['Referer'] = f'{self.host}:{self.port}/objecttracker'
        data = {
            'p': str(pipeline_id),
            's': str(stage_id),
            'suppress': '',
            'keytype': 'patient',
            'keys': key,
            'format': 'csv'
        }
        response = self.post('objecttracker',
                             headers=headers,
                             data=data)
        if response.status_code != 200:
            logging.debug(response.text)
            return None
        logging.debug(f'Results: {response.text}')

        object_tracker_dict = parse_object_tracker_results(response.text, patient_id, study_uid_filter)
        return object_tracker_dict

    def idmap_search(self, pipeline_id, stage_id, key, keytype):
        headers = self.headers.copy()
        headers['Referer'] = f'{self.host}:{self.port}/idmap'
        data ={
            "p": str(pipeline_id),
            "s": str(stage_id),
            "suppress": "",
            "keytype": keytype,
            "keys": str(key),
            "format": "csv"
        }
        logging.debug(f'Querying ID-map at {pipeline_id};{stage_id}')
        response = self.session.post(f'{self.host}:{self.port}/idmap',
                                 headers=headers,
                                 data=data)
        if response.status_code != 200:
            logging.debug(f'Got {response.status_code}')
            logging.debug(response.text)
            return None

        new_id = parse_idmap_results(response.text)
        return new_id

    def idmap_search_uid(self, pipeline_id, stage_id, key):
        return self.idmap_search(pipeline_id, stage_id, key, keytype="originalUID")

    def idmap_reverse_search_uid(self, pipeline_id, stage_id, key):
        return self.idmap_search(pipeline_id, stage_id, key, keytype="trialUID")

    def idmap_search_patientid(self, pipeline_id, stage_id, key):
        return self.idmap_search(pipeline_id, stage_id, key, keytype="originalPtID")

    def idmap_reverse_search_patientid(self, pipeline_id, stage_id, key):
        return self.idmap_search(pipeline_id, stage_id, key, keytype="trialPtID")

    def find_object_tracker_stages(self, pipeline):
        object_trackers = [stage for stage in pipeline.stages.items() if isinstance(stage[1], ObjectTracker)]
        if object_trackers:
            return object_trackers
        else:
            raise exceptions.CTPYNoObjectTrackerFound(f"No ObjectTracker stages found in pipeline {pipeline.pipeline_id}!")
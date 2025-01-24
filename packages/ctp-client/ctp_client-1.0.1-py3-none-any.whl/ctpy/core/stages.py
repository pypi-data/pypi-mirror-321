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


import logging

from ctpy import exceptions
from ctpy.helpers import parse_idmap_results, parse_object_tracker_results


class StageFactory:
    @classmethod
    def create_stage(cls, pipeline, stage_id, stage_config):
        stage_class = stage_config['class'].split('.')[-1]

        sanitized_config = cls._sanitize_config(stage_config)
        logging.debug('Creating stage: %s', stage_class)
        logging.debug('Creating stage: %s', sanitized_config)

        if stage_class == 'IDMap':
            return IDMap(pipeline, stage_id, **sanitized_config)
        if stage_class == 'DicomAnonymizer':
            return DicomAnonymizer(pipeline, stage_id, **sanitized_config)
        if stage_class == 'DicomFilter':
            return DicomFilter(pipeline, stage_id, **sanitized_config)
        if stage_class == 'DicomPixelAnonymizer':
            return DicomPixelAnonymizer(pipeline, stage_id, **sanitized_config)
        if stage_class == 'ObjectTracker':
            return ObjectTracker(pipeline, stage_id, **sanitized_config)

        return BaseStage(pipeline, stage_id, **sanitized_config)

    @classmethod
    def _sanitize_config(cls, stage_config):
        sanitized_config = {}
        if 'class' not in stage_config or 'root' not in stage_config:
            raise exceptions.CTPYStageParseError
        sanitized_config['stage_class'] = stage_config['class']
        sanitized_config['root'] = stage_config['root']

        accepted_keys = ['id', 'root', 'quarantine', 'lookup_table', 'script', 'name', 'script']

        for key in accepted_keys:
            if key in stage_config:
                sanitized_config[key] = stage_config[key]
        return sanitized_config


class BaseStage():
    def __init__(self, pipeline, stage_id, stage_class, root, id=None, quarantine=None, name=None):
        self.id = id
        self.stage_id = stage_id
        self.pipeline = pipeline
        self.stage_class = stage_class
        self.root = root
        self.quarantine = quarantine
        self.name = name

    def __str__(self):
        return f'This Stage is of type: {type(self).__name__}'


class ObjectTracker(BaseStage):
    def query_patientids(self, key, study_uid_filter=None):
        headers = {}
        headers['Referer'] = self.pipeline.server.ctpy_session.format_uri('/objecttracker')
        data = {
            'p': str(self.pipeline.pipeline_id),
            's': str(self.id),
            'suppress': '',
            'keytype': 'patient',
            'keys': key,
            'format': 'csv'
        }
        response = self.pipeline.server.ctpy_session.post('objecttracker',
                             headers=headers,
                             data=data)
        if response.status_code != 200:
            logging.debug(response.text)
            return None
        object_tracker_dict = parse_object_tracker_results(response.text, study_uid_filter)
        return object_tracker_dict


class IDMap(BaseStage):
    def search(self, key, keytype):
        headers = {}
        headers['Referer'] = self.pipeline.server.ctpy_session.format_uri('/idmap')
        data ={
            'p': str(self.pipeline.pipeline_id),
            's': str(self.id),
            "suppress": "",
            "keytype": keytype,
            "keys": str(key),
            "format": "csv"
        }

        response = self.pipeline.server.ctpy_session.post('idmap',
                                 headers=headers,
                                 data=data)
        if response.status_code != 200:
            logging.debug(response.text)
            return None

        new_id = parse_idmap_results(response.text)
        return new_id


class DicomFilter(BaseStage):
    def __init__(self, pipeline, stage_id, stage_class, root,
                 id=None, name=None, quarantine=None, script=None):
        super().__init__(pipeline, stage_class, root, name, quarantine=quarantine, name=name, id=id)
        self.script = script


class DicomAnonymizer(BaseStage):
    def __init__(self, pipeline, stage_id, stage_class, root, id,
                 name=None, quarantine=None, script=None, lookup_table=None):
        super().__init__(pipeline, stage_id, stage_class, root, quarantine=quarantine, name=name, id=id)
        self.lookup_table = lookup_table
        self.script = script

    def add_key(self, key, value):
        query = f'id={self.id}&key={key}&value={value}'
        response = self.pipeline.server.ctpy_session.put('/lookup', query)
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

class DicomPixelAnonymizer(BaseStage):
    def __init__(self, pipeline, stage_id, stage_class,
                 name=None, root=None, quarantine=None, script=None):
        super().__init__(pipeline, stage_class, root, name)
        self.script = script

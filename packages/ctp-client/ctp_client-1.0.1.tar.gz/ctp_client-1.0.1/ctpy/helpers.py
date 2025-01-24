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

from time import sleep, time
import logging
import datetime
from typing import Dict, List, Optional, Union

import bs4
from pydantic import BaseModel, Field, AliasChoices, field_validator


def parse_object_tracker_results(object_tracker_string: str,
                                 patient_id_filter: Optional[str] = None,
                                 study_uid_filter: Optional[str] = None) -> Union[None, Dict[str, Dict[str, Dict[str, str]]]]:
    try:
        data = object_tracker_string.split()[1:]
    except IndexError:
        return None
    object_tracker_dict = {}
    for row in data:
        row = row.split(',')
        patient_id = row[0]
        study_uid = row[1]
        series_uid = row[2]
        instances = int(row[3])
        if patient_id_filter and not patient_id == patient_id_filter:
            logging.debug('Filtering Patient: %s not equal: %s', patient_id, patient_id_filter)
            continue
        if study_uid_filter and not study_uid == study_uid_filter:
            logging.debug('Filtering StudyUID: %s', study_uid, study_uid_filter)
            continue
        if patient_id in object_tracker_dict:
            if study_uid in object_tracker_dict[patient_id]:
                if series_uid in object_tracker_dict[patient_id][study_uid]:
                    object_tracker_dict[patient_id][study_uid][series_uid] = instances
                    logging.debug('Update %s to object_tracker_dict', instances)
                else:
                    object_tracker_dict[patient_id][study_uid][series_uid] = instances
                    logging.debug('Add %s to object_tracker_dict', instances)
            else:
                object_tracker_dict[patient_id][study_uid] = {series_uid: instances}
                logging.debug('Add %s|%s;%s to object_tracker_dict',
                                study_uid, series_uid, instances)
        else:
            logging.debug('Add %s|%s|%s;%s to object_tracker_dict',
                            patient_id, study_uid, series_uid, instances)
            object_tracker_dict[patient_id] = {study_uid: {series_uid: instances}}
    return object_tracker_dict


def parse_idmap_results(idmap_string: str) -> Union[None, str]:
    logging.debug(f'idmap: {idmap_string}')
    lines = idmap_string.split('\n')
    _, new = lines[1].split(',')

    if new.startswith('=("'):
        trial_uid = new[3:-2]
        return trial_uid
    return None


def poll_object_tracker_for_studyuid(ctpy_session, pipeline_id,
                                     object_tracker_id, patient_id,
                                     study_uid, delay, timeout):
    old_data = object_tracker_data = {}
    last_update = int(time())
    logging.debug(f'Querying for patient:{patient_id}, study_uid: {study_uid}')
    while old_data == object_tracker_data:
        object_tracker_data = ctpy_session.get_object_tracker_patient_info(pipeline_id,
                                                                           object_tracker_id,
                                                                           '',
                                                                           patient_id,
                                                                           study_uid)
        logging.debug('Checking for new data...')
        if old_data == object_tracker_data:
            logging.debug('No incoming data check timeout')
            if int(time() - last_update) > timeout:
                logging.debug('Timeout reached')
                break
        else:
            last_update = int(time())
            logging.debug('Incoming data...')
            logging.debug(f'Found: {object_tracker_data}')

        old_data = object_tracker_data
        sleep(delay)

    return object_tracker_data


class CtpSummary(BaseModel):
    pipeline: str = Field('', validation_alias=AliasChoices('Pipeline'))
    import_queues: int = Field(0, validation_alias=AliasChoices('ImportQueues'))
    export_queues: int = Field(0, validation_alias=AliasChoices('ExportQueues'))
    quarantines: int = Field(0, validation_alias=AliasChoices('Quarantines'))
    time_stamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now())  # pylint:disable=unnecessary-lambda

    def __init__(self, row):
        super().__init__()
        values = row.find_all('td')
        self.pipeline = values[0].text
        self.import_queues = int(values[1].text)
        self.export_queues = int(values[2].text)
        self.quarantines = int(values[3].text)

    @field_validator('import_queues', 'export_queues', 'quarantines', mode='before')
    @classmethod
    def remove_separators(cls, v: str) -> int:
        if isinstance(v, int):
            return v
        return int(v.replace(',', ''))
    
    def to_table_row(self) -> List:
        return [self.pipeline, self.import_queues, self.export_queues, self.quarantines]


def parse_summary(html: Union[str, bytes]) -> Union[None, List[CtpSummary]]:
    soup = bs4.BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', attrs={'class': 'summary'})
    if len(tables) != 1:
        return None

    rows = tables[0].find_all('tr')
    results = [CtpSummary(row) for row in rows[1:]]

    return results


def parse_step(html: Union[str, bytes]) -> Dict[str, Dict[str, str]]:
    soup = bs4.BeautifulSoup(html, 'html.parser')

    status_table = soup.find('h2', string='Status').find_next_sibling('table')
    config_table = soup.find('h2', string='Configuration').find_next_sibling('table')

    return {
        'status': parse_vertical_table(status_table),
        'config': parse_vertical_table(config_table),
    }


def parse_vertical_table(table_element: bs4.Tag) -> Dict[str, str]:
    """
    Parse the vertical tables that just have 2 columns with a key-value structure

    :param table_element: table DOM element
    :return: table parsed into a dict
    """
    rows = table_element.find_all('tr')

    result = {}
    for row in rows:
        elements = row.find_all('td')
        if len(elements) != 2:
            raise ValueError('Expected table to have 2 columns only!')

        result[elements[0].text] = elements[1].text

    return result


def summarize_object_tracker_content(object_tracker_content):
    subjects = 0
    experiments = 0
    scans = 0
    instances = 0
    for _, subject_info in object_tracker_content.items():
        subjects += 1
        for _, experiment_info in subject_info.items():
            experiments += 1
            for _, scan_instances in experiment_info.items():
                scans += 1
                instances += scan_instances

    return subjects, experiments, scans, instances

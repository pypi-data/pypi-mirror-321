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

from ctpy.core.stages import StageFactory


class Pipeline():
    def __init__(self, server, pipeline_id, pipeline):
        self.server = server
        self.pipeline_id = pipeline_id
        self.stages = {}
        for stage_id, stage in enumerate(pipeline):
            logging.debug('Create stage:<%s> <%s>', stage_id, stage)
            ctp_stage = StageFactory.create_stage(self, stage_id, stage.attrib)
            if id in stage.attrib:
                self.stages[stage.attrib['id']] = ctp_stage
            else:
                self.stages[stage_id] = ctp_stage

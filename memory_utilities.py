'''
memory_utilities.py

General memory helpers

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

import os
import sys

from logger import Logger

'''
Global definitions
'''
global_logger = Logger(__file__)


'''
Query disk space information for a directory in GB
'''
def get_dir_space(dir):

    stats = os.statvfs(dir)
    total = stats.f_frsize * stats.f_blocks
    free = stats.f_frsize * stats.f_bfree
    available = stats.f_frsize * stats.f_bavail    

    return total / 1e9, free / 1e9, available / 1e9
    
def show_dir_space(dir):
    
    msg = get_dir_space_descriptor(dir)
    global_logger.log('Directory memory stats for', dir, msg)

def get_dir_space_descriptor(dir):

return 'Total: ' + str(total) + 'GB, free: ' + str(free) + 'GB, available: ' + str(avail) + 'GB'
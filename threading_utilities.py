'''
threading_utilities.py

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

import time
import datetime
        
'''
Wait for function to evaluate true or timeout before returning
'''
def wait_for_or_complete(i_timeout_us, i_fnc, *i_kargs):

    ret = False
    start = datetime.datetime.now()
    delta = start - start
    
    while not ret and delta.microseconds <= i_timeout_us:
        ret = i_fnc(*i_kargs)
        delta = datetime.datetime.now() - start

    return ret
    
'''
Wait for function to evaluate true or until a specified clock time before returning
'''
def wait_until_or_complete(i_end_time, i_fnc, *i_kargs):

    ret = False

    while not ret and time.time() < i_end_time:
        ret = i_fnc(*i_kargs)

    return ret
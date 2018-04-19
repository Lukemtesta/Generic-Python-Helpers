'''
datetime_utilities.py

General datetime helper functions

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

import datetime

'''
Create timestamp
'''
def compute_timestamp():
        
    return datetime.datetime.now()
      
'''
Convert timestamp to string 
'''   
def timestamp_to_string(i_timestamp):
    
    return i_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
'''
Convert string in format years-months-days hours-minutes-seconds to timestamp
'''   
def string_to_timestamp(i_timestamp):

    return datetime.datetime.strptime(i_timestamp, '%Y-%m-%d %H:%M:%S')
    
'''
Calculate the difference between two timestamps in seconds
'''   
def compare_time_seconds(i_time_start, i_time_end):

    delta = i_time_end - i_time_start
    return (60*60*24 - delta.seconds)
    
'''
Calculate the difference between two timestamps in minutes
'''   
def compare_time_minutes(i_time_start, i_time_end):

    return compare_time_seconds(i_time_start, i_time_end) / 60
    
'''
Add two timestamps 
'''
def add_time(i_time_a, i_time_b):

    return datetime.datetime.combine(i_time_a, i_time_b)
    
'''
Add seconds to timestamp
'''
def add_time_seconds(i_time, i_seconds):

    return i_time + datetime.timedelta(seconds=i_seconds)
    
'''
Calculate the difference between two timestamps in minutes
'''   
def compare_time_hours(i_time_start, i_time_end):

    return compare_time_minutes(i_time_start, i_time_end) / 60

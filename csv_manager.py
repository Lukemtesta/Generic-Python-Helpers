'''
csv_manager.py

Python CSV reader and writer

Dependencies:

Python 3.0+

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

import csv
import os.path

from log import Logger


'''
Global definitions
'''
global_logger = Logger(__file__)


'''
Generic CSV file handler
'''
class CSVManager():

    def __init__(self, i_filename, i_overwrite = False, i_encoding = 'utf8', i_delimiter = ','):
    
        self.filename = i_filename
        self.delimiter = i_delimiter
        self.encoding = i_encoding
        self.overwrite = i_overwrite
        
        self.set_overwrite(i_overwrite)
        
        if i_overwrite and os.path.exists(i_filename):
            os.remove(i_filename)
            
        self.data = self.read()
        self.lineptr = len(self.data)
        
    def does_file_exist(self):
    
        return os.path.exists(self.filename)
        
    def is_file(self):
    
        return os.path.isfile(self.filename)
        
    def read_row(self, i_index):
                
        return [ row[i_index] for row in self.read() ]
        
    def read_formatted(self):
    
        rows = self.read()
        
        return [row.split(self.delimiter) for row in rows]
        
    def read(self):
    
        ret = []
                
        if not os.path.isfile(self.filename):
            return ret
    
        with open(self.filename, 'r', encoding=self.encoding) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self.delimiter)
            
            for row in spamreader:
                ret.append(row)
                                
        return ret[1:]
        
    def verify_dir(self):
    
        dir = os.path.dirname(self.filename)

        if not os.path.exists(dir) and dir:
            os.makedirs(dir)
        
    def write_rows(self, i_rows):
    
        self.verify_dir()
        overwrite = self.overwrite
        
        if not os.path.exists(self.filename):
            self.set_overwrite(True)
            
        with open(self.filename, self.write_mode, newline='') as csvfile:
            spamwriter = csv.writer(
            csvfile, 
            delimiter=self.delimiter, 
            quotechar='|', 
            quoting=csv.QUOTE_MINIMAL)
            
            spamwriter.writerows( i_rows )
                                    
        [ self.data.append(row) for row in i_rows ]
            
        self.set_overwrite(overwrite)
            
    def write_row_cache(self, i_row):
    
        if not isinstance(i_row, list):
            i_row = [i_row]
            
        self.data.append(i_row)
        
    def clear_row_cache(self):
    
        self.lineptr = 0
        self.data = []
            
    def set_overwrite(self, i_overwrite):
        
        self.overwrite = i_overwrite
        
        # work around new line carriage return for windows
        self.write_mode = 'a' 
        if i_overwrite:
            self.write_mode = 'w'
            
    def update_file_buffer(self):
    
        overwrite = self.overwrite
        self.set_overwrite(False)
        
        self.write_rows(self.data[self.lineptr:])
            
        self.set_overwrite(overwrite)
                    
    def get_filename(self):
    
        return self.filename

    def show(self):
    
        ret = []
    
        if os.path.isfile(self.filename):
            ret = self.read()
    
        show(ret)
                
    def get_headers(self):
    
        ret = self.read()
                
        if len(ret) > 0:
            ret = ret[0]
        
        return ret
        
    def get_filename(self):
    
        return self.filename
        
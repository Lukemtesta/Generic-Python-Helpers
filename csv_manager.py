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


'''
Generic CSV file handler
'''
class CSVManager():

    def __init__(self, i_filename, i_overwrite = False, i_encoding = 'utf8', i_delimiter = ','):
    
        self.filename = i_filename
        self.delimiter = i_delimiter
		self.encoding = i_encoding
        
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
    
        ret = []
                
        if not os.path.isfile(self.filename):
            return ret
    
        with open(self.filename, 'r', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self.delimiter, quotechar='|')
            
            for row in spamreader:
                ret.append(row.split(self.delimiter))
                                
        return ret[1:]
        
    def read(self):
    
        ret = []
                
        if not os.path.isfile(self.filename):
            return ret
    
        with open(self.filename, 'r', encoding=self.encoding) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self.delimiter, quotechar='|')
            
            for row in spamreader:
                ret.append(row)
                                
        return ret[1:]
        
    def write_row(self, i_row):
            
        with open(self.filename, self.write_mode, newline='') as csvfile:
            spamwriter = csv.writer(
            csvfile, 
            delimiter=self.delimiter, 
            quotechar='|', 
            quoting=csv.QUOTE_MINIMAL)
            
            spamwriter.writerow( i_row )
			self.data.append(i_row)
			
	def write_row_cache(self, i_row):
            
        self.data.append(i_row)
		
	def clear_row_cache(self):
	
		self.lineptr = 0
		self.data = []
            
    def set_overwrite(self, i_overwrite):
        
        # work around new line carriage return for windows
        self.write_mode = 'a' 
        if i_overwrite:
            self.write_mode = 'w'
			
	def update_file_buffer_with_cache(self):
    
		overwrite = self.overwrite
        self.set_overwrite(False)
		
        for data in self.data[self.lineptr:]:
            self.write_row(data)
			
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
        
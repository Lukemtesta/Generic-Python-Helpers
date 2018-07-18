'''
file_manager.py

Python generic file reader and writer

-Licensed to the Apache Software Foundation (ASF) under one
-or more contributor license agreements.  See the NOTICE file
-distributed with this work for additional information
-regarding copyright ownership.  The ASF licenses this file
-to you under the Apache License, Version 2.0 (the
-"License"); you may not use this file except in compliance
-with the License.  You may obtain a copy of the License at
+License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e
 
-  http://www.apache.org/licenses/LICENSE-2.0
-
-Unless required by applicable law or agreed to in writing,
-software distributed under the License is distributed on an
-"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
-KIND, either express or implied.  See the License for the
-specific language governing permissions and limitations
-under the License.
'''

import os.path


'''
Generic file handler
'''
class FileManager():

    def __init__(self, i_filename, i_overwrite = False):
    
        self.filename = i_filename
        self.delimiter = ','
        self.data = []
        
        self.set_overwrite(i_overwrite)
        
    def read(self):
            
        if not os.path.isfile(self.filename):
            self.data = []
            return self.data
    
        with open(self.filename, 'r') as file:
            self.data = file.read()

        return self.data
        
    def write(self, row):
        
        with open(self.filename, self.write_mode) as file:
            self.data.append(row)
            file.write(row)
            
    def set_overwrite(self, i_overwrite):
    
        self.write_mode = 'a'
        if i_overwrite:
            self.write_mode = 'w'

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
        
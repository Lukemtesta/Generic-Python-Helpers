'''
file_manager.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e

Python generic file reader and writer
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
        
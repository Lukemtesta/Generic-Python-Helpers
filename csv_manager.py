'''
csv_manager.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e

Python CSV reader and writer
'''

import csv
import os.path


'''
Generic CSV file handler
'''
class CSVManager():

    def __init__(self, i_filename, i_overwrite = False):
    
        self.filename = i_filename
        self.delimiter = ','
        
        self.set_overwrite(i_overwrite)
        
    def read(self):
    
        ret = []
        
        if not os.path.isfile(self.filename):
            return ret
    
        with open(self.filename, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self.delimiter, quotechar='|')
            
            for row in spamreader:
                ret.append(row)

        return ret[:-1]
        
    def write_row(self, row):
        
        with open(self.filename, self.write_mode) as csvfile:
            spamwriter = csv.writer(
            csvfile, 
            delimiter=self.delimiter, 
            quotechar='|', 
            quoting=csv.QUOTE_MINIMAL)
            
            spamwriter.writerow( row )
            
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
        
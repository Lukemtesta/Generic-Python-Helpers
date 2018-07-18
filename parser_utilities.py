'''
parser_utilities.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e
'''

import argparse

'''
Evaluation for command line boolean parsing
'''
def string_to_bool(i_string):
    
    ret = False
    
    i_string = i_string.lower()

    if i_string in ('true', '1'):
        ret = True
    elif not i_string in ('false', '0'):
        raise argparse.ArgumentTypeError('Boolean value expected. Must be parsed as true or false')

    return ret
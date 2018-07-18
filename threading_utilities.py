'''
threading_utilities.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e
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
'''
Numerical.py

License: https://www.binpress.com/license/view/l/89b074d75c23539f3ad7fd68da6fc07e

General maths library
'''

import math
  
    
'''
Round down to N decimal places
'''
def floor_decimals(i_value, i_sig_fig):
    
    assert(i_sig_fig >= 1)
    coeff = math.pow(10, i_sig_fig)
    
    if coeff == 0:
        return 0
    else:
        return math.floor(i_value * coeff) / coeff

'''
Round up to N decimal places
'''
def ceil_decimals(i_value, i_sig_fig):
    
    assert(i_sig_fig >= 1)
    coeff = math.pow(10, i_sig_fig)
    
    if coeff == 0:
        return 0
    else:
        return math.ceil(i_value * coeff) / coeff
    
        

    


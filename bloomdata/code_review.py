### IN style_example.py FILE###
'''
This is my module docstring.
'''

#what would you say if you were working with someone and this is the code they gave you?

import math
import sys

def exampl1():
    '''
    This function represents example 1
    '''
  ### THIS IS A LONG COMMENT AND should be wrapped to fit within a 72 character limit
    some_tuple =( 1,2, 3,'a'  )
    some_variable={"long":'LONG CODE LINES should be wrapped within 79 characters',
                   'other':[math.pi, 100,200, 300, 9999292929292, 
                   "This IS a long string that looks gross and goes beyond what it should"],
                   "more": {"inner": "THIS whole logical line should be wrapped"},
                   "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]}

    return (some_tuple, some_variable)

def example_2():
    '''
    This is example 2
    '''
    return {"has_key() is deprecated": True}


class Example3(object):
    '''
    This class represents example 3
    '''
def __init__   (self, bar):
    bar+= 1
    bar=bar* bar 
    return bar

some_string = """
                  INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented,
THIS IS MORE CODE
"""
    
    return (sys.path, some_string)
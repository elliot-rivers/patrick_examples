'''`module.py` doesnt' mean anything as a name

just an example of a name. here's where i'm putting 
a lot of the actual meat
'''
from .util import helper_function_whatever

def an_important_function(data_1: int, data_2: float):
    data_3 = helper_function_whatever(data_1, data_2)
    return data_1 * data_2 * data_3

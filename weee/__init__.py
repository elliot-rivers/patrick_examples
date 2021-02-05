'''Stuff here is what external users who `import` my module see

So put the stuff important to how they use the module in here.
Hide the rest. They could still access it if they wanted
'''
from .util import aa, bb, cc

def friendly_function(mat, field1, field2):
    a = aa(mat)
    b = bb(field1)
    c = cc(mat, field2)

    return a + b + c

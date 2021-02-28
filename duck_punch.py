import sys

class Something:
    '''A class with a method to write'''
    def __init__(self):
        self.foo = 333

    def write(self, outfile):
        outfile.write('{}\n'.format(self.foo))

# Pretend this is a file
output_file = sys.stdout

# Instantiate Something and write. All is well
s = Something()
s.write(output_file)

def save_obj_to_output(obj, output):
    ...
    obj.save(output)
    ...

try:
    save_obj_to_output(s, output_file)
except AttributeError:
    print('oopsie')
else:
    print('woohoo')

## What to do?
import types
# Use the types module

# Duck punch
def duck_punch_save(self, output_file):
    self.write(output_file)

# Add a new method after instantiation :D
s.save = types.MethodType(duck_punch_save, s)

# Now does this work?
try:
    save_obj_to_output(s, output_file)
except AttributeError:
    print('oopsie')
else:
    print('woohoo')


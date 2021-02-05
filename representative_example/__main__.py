'''This is useful for providing a reference implementation of 
using your stuff

If you're sitting at the terminal and you aren't consuming my
function downstream -- just poking data through it -- then here's
a "good enough" version

This is where specific I/O should be handled. If you want to support .mat files or .json or whatever, do that here. Your function be in terms of just the _data_
'''

from . import an_important_function

def main():
    '''This main just runs with hard-coded values'''
    ans = an_important_function(2, 3)
    print('The important answer is:', ans)
    return 0

if __name__ == '__main__':
    main()

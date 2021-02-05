'''This is useful for providing a reference implementation of 
using your stuff

If you're sitting at the terminal and you aren't consuming my
function downstream -- just poking data through it -- then here's
a "good enough" version

This is where specific I/O should be handled. If you want to support .mat files or .json or whatever, do that here. Your function be in terms of just the _data_
'''
from argparse import ArgumentParser

from . import an_important_function

def main():
    '''This main runs with CLI arguments'''
    parser = ArgumentParser(description=
            'Very useful, representative example of stuff')
    parser.add_argument('-d1', type=int, help='1 value', required=True)
    parser.add_argument('-d2', type=float, help='2 value', default=1.0)
    args = parser.parse_args()

    ans = an_important_function(args.d1, args.d2)
    print('The important answer is:', ans)
    return 0

if __name__ == '__main__':
    main()

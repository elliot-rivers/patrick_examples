'''This is useful for providing a reference implementation of 
using your stuff

If you're sitting at the terminal and you aren't consuming my
function downstream -- just poking data through it -- then here's
a "good enough" version

This is where specific I/O should be handled. If you want to support .mat files or .json or whatever, do that here. Your function be in terms of just the _data_
'''
from argparse import ArgumentParser
import scipy.io

from . import friendly_function

def main():
    '''This main runs with file input happening'''
    parser = ArgumentParser(description=
            'Very useful, representative example of stuff')
    parser.add_argument('--mat_file', type=str, required=True,
            help='where to read data from')
    args = parser.parse_args()

    data = scipy.io.loadmat(args.mat_file)

    ans = friendly_function(data['aa'], data['field1'], data['field2'])
    print(ans)
    return 0

if __name__ == '__main__':
    main()

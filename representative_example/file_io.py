'''This is useful for providing a reference implementation of 
using your stuff

If you're sitting at the terminal and you aren't consuming my
function downstream -- just poking data through it -- then here's
a "good enough" version

This is where specific I/O should be handled. If you want to support .mat files or .json or whatever, do that here. Your function be in terms of just the _data_
'''
from argparse import ArgumentParser
import json

from . import an_important_function

def main():
    '''This main runs with file input happening'''
    parser = ArgumentParser(description=
            'Very useful, representative example of stuff')
    parser.add_argument('--json_file', type=str, required=True,
            help='where to read data from')
    args = parser.parse_args()

    with open(args.json_file) as f:
        data = json.load(f)

    ans = an_important_function(data['data_1'], data['data_2'])
    print('The important answer is:', ans)
    return 0

if __name__ == '__main__':
    main()

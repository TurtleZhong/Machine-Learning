#! /usr/bin/python
# Filename: test1.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

import test

test.func(50)

from test import func2

func2()

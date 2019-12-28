#!/usr/bin/python
#-*- encoding: utf-8 -*-

import pprint
import sys

if sys.version_info.major < 3:
    print( 'Upgrade to Python 3' )
    exit(1)

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":

    print("Main")
    exit(0)

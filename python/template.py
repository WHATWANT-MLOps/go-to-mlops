#!/usr/bin/python
#-*- encoding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if sys.version_info.major < 3:
    print( 'Upgrade to Python 3' )
    exit(1)


if __name__ == "__main__":

    print("Main")
    exit(0)

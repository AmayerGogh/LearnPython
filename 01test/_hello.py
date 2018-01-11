#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a test module'

__auhor__="Amayer Gogh"

import sys

def test():
    args =sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello  %s!' % args[1])
        print('Hello, %s!' % args[1])
    else:
        print('to many')

if __name__=='__main__':
    test()
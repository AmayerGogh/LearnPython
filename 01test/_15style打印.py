# -*- coding: UTF-8 -*-

def print_red(str):
    print('\033[4;31m %s \033[0m' % str)

print_red('tests')    
input('')
#!/usr/bin/python3

import re
import sys
import os
import argparse

def main():
    # Add the ability to take a file as an argument
    # parser = argparse.ArgumentParser(description='List of passwords to convert to masks')
    # parser.add_argument('-f', default=1, type=str)
    # Get file as variable to use later
    passFile = open('tests')
    passFile = passFile.read()
    convert(passFile)

def convert(i):
    print(i)

main()

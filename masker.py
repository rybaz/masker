#!/usr/bin/python3

import argparse

# Add the ability to take a file as an argument
parser = argparse.ArgumentParser(description='List of passwords to convert to masks')
parser.add_argument('-f', default=1, type=str)
# Get file as variable to use later
passFile = 'tests.txt'

def main():
    # Print out new passfile
    print("New mask list:" + "\n")
    convert(passFile)

def convert(i):

    with open(i) as file:
        for line in file:
            list1 = list(line)
            masklist = ""
            # Remove last item in list since it will always be a newline character
            del list1[-1]
            for n, char in enumerate(list1):
                if char.isupper():
                    list1[n] = "?u"
                elif char.islower():
                    list1[n] = "?l"
                elif char.isdigit():
                    list1[n] = "?d"
                else:
                    list1[n] = "?s"
            # Join broken lines back to strings
            masklist = masklist.join(list1)
            print(masklist)

main()

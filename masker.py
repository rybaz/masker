#!/usr/bin/python3

import argparse
import collections

# Get file as variable to use later
passFile = 'passwords.txt'
outFile = 'results.txt'

def main():

    print("[*] Converting passwords to masks..." + "\n")
    convertAndSort(passFile)
    # Print out new passfile
    print("[*] Count and frequency results printed to: " + outFile + "\n")

def convertAndSort(i): # Converting input list to hashcat masks and running analysis

    # Character conversion
    with open(i) as file:
        for line in file:
            list1 = list(line)
            maskList = ""
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
            
            # Writing masks to results.txt
            with open('results.txt', 'a+') as outFile:
                # Join broken lines back to strings
                maskList = maskList.join(list1)
                outFile.write(maskList + "\n")

            outFile.close()

if __name__== "__main__":
  main()

#! /usr/bin/env python
#coding=utf-8

import sys
import os
import re
from random import randint

path = 'Data/' # where the data is stored
fPtn = 'First' # pattern for first name filenames
lPtn = 'Last'  # pattern for last name filenames
delimiter = ','  # the symbol that splits names

# get specific data files given a pattern
def getFiles(files, ptn):
    result = []
    for fileName in files:
        if re.match(ptn, fileName) != None:
            result.append(fileName)
    return result

# retrieve all the names in a file list, returns a name list
def getNames(path, files, delimiter):
    result = []
    for fileName in files:
        f = open(path + fileName,'r')
        data = f.read().replace('\n','')
        result = result + data.split(delimiter)
        f.close()
    return result

# randomly generates a name
def generate(fList, lList, firstNameLength = 0):
    if firstNameLength > 3:
        print 'Warning: Common Chinese Names are between 2~4 characters'
    if firstNameLength < 1: # Chinese names are at least two characters long
        firstNameLength = randint(1,2)
    firstName = ''
    while firstNameLength > 0:
        firstName = firstName + fList[randint(0,len(fList)-1)]
        firstNameLength = firstNameLength - 1   
    return lList[randint(0,len(fList)-1)] + firstName

def main():
    listing = os.listdir(path)
    firstNamesFiles = getFiles(listing, fPtn)
    lastNamesFiles = getFiles(listing, lPtn)
    firstNames = getNames(path, firstNamesFiles, ',')
    lastNames = getNames(path, lastNamesFiles, ',')
    print generate(firstNames, lastNames)
    
if __name__ == "__main__":
    main()

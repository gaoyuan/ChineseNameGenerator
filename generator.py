#! /usr/bin/env python
#coding=utf-8

import sys
import os
import re
import argparse
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
def generate(fList, lList, firstNameLength = 0, first = '', last = ''):
    
    # length check and suggestions
    if firstNameLength > 3:
        print 'Warning: Common Chinese Names are between 2~4 characters'
    if firstNameLength < 1: # Chinese names are at least two characters long
        firstNameLength = randint(1,2)
    
    # generating the firstname character by character
    firstName = ''
    while firstNameLength > 0:
        firstName = firstName + fList[randint(0,len(fList)-1)]
        firstNameLength = firstNameLength - 1
    lastName = lList[randint(0,len(fList)-1)]
    
    # if first and/or last name is specified, use it
    if first != ''
        firstName = first
    if last != ''
        lastName = last
    
    # return the name generated
    return  lastName + firstName

def main():
    # parse the argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', metavar = 'Integer',type = int, default = 0,
        help = 'specify the length of first name, if < 1, then randomly choose 1 or 2')
    parser.add_argument('-first', metavar - 'String', type = String, default = '',
                        help = 'specify the first name')
    parser.add_argument('-last', metavar - 'String', type = String, default = '',
                        help = 'specify the last name')
    args = parser.parse_args()
    
    listing = os.listdir(path) # get the filenames in the data path
    firstNamesFiles = getFiles(listing, fPtn) # data files with first names
    lastNamesFiles = getFiles(listing, lPtn) # data files with last names
    firstNames = getNames(path, firstNamesFiles, ',') # get all the first names
    lastNames = getNames(path, lastNamesFiles, ',') # get all the last names
    
    # print the generated name
    print generate(firstNames, lastNames, args. l, first, last)
    
if __name__ == "__main__":
    sys.exit(main())

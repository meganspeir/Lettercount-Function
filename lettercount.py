# lettercount.py
# A Python script that counts every letter in a given text.
# http://www.meganspeir.com
#
# Copyright (C) 2013 Megan Speir. All rights reserved.
#
# Licensed under The BSD 3-Clause License. You may not use this file except
# in compliance with the License. You may obtain a copy of the License at
# http://opensource.org/licenses/BSD-3-Clause

from sys import argv

script, inputfile = argv

#opens file from input
f = open(inputfile)
filetext = f.read()
f.close()

#initializes list with default value 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettercount = [0] * 26

#loop through filetext to count char
for char in filetext.lower():
   if char in alphabet:
        index = alphabet.index(char)
        lettercount[index] += 1

for count in lettercount:
    print count

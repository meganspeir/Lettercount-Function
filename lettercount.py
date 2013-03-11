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

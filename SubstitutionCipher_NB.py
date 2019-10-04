#!/usr/bin/python3
#
# Nikki Benoit
# Aug 12 2019  21:56:42.5642 MDT
#
######################################
# Do a frequency analysis on a block of ciphertext in a txt file
######################################
#
from collections import OrderedDict
from operator import itemgetter

# Create dictionary to hold each character as key and count as value
characters = {}

# Read text file loop by line to get each character
with open("Substitution.txt") as cipherText:
    for line in cipherText:
        for char in line:
            # Ignore spaces
            if(char == " "):
                continue
            # If character is already a key, add 1 to count
            elif(char in characters.keys()):
                characters[char] += 1
            # If character is not a key, add and set count to 1
            else:
                characters[char] = 1

# Order dictionary by letter with descending count
sortedChars = OrderedDict(sorted(characters.items(), key=itemgetter(1), reverse = True))

# # Print ordered dictionary
for alpha, times in sortedChars.items():
    print(alpha + " happens " + str(times))

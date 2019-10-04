#!/usr/python3
#
# Nikki Benoit
# Aug 14 2019  15:57:22.5722 MST
#
#####################################
 # Encrypt using permutation cipher and then decrypt
#####################################
import string
import numpy

# Get plaintext and key
plaintext = "Mary had a little lamb, its fleece as white as snow. \
            Everywhere that Mary went, the lamb was sure to go".upper()
key = "Breaking".upper()
keyLength = len(key)

########## WORKS IN LINUX ###########
# Remove whitespace and punctuation
plaintext = plaintext.replace(" ", "")
plaintext = plaintext.translate(None, string.punctuation)
# Get length
ptLength = len(plaintext)

######### WORKS IN WINDOWS ##########
# Remove whitespace and punctuation and store in a new variable
# newPT = ""
#
# for char in plaintext:
#     if(char in string.punctuation or char == " "):
#         continue
#     else:
#         newPT += char
# # Get length
# ptLength = len(newPT)


# Create numpy array for use with argsort to get key 'new' indicies
keyArray = numpy.array([ list(char) for char in key ])
# Array for key sort order
sortOrder = keyArray.argsort(axis=0)

# Pad message with X if plaintext length doesn't match key length
while(ptLength % keyLength != 0):
    plaintext += "X"
    ptLength += 1

numBlocks = ptLength / keyLength

# Section plaintext into 2D list by length of key
cipherText = [plaintext[i:i+keyLength] for i in range(0, ptLength, keyLength)]
# STDOUT cipher
cipher_out = ""

# Print cipherText using sortOrder indicies for columns
for row in range(len(cipherText)):
    for col in range(len(cipherText[row])):
        cipher_out += cipherText[row][int(sortOrder[col])]

print(cipher_out)

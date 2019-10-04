#!/usr/bin/python3
#
# Nikki Benoit
# Aug 12 2019  15:56:30.5630 MDT
#
######################################
# Encrypt plaintext using a Caesar Cipher based on a given rotation and then decrypt
######################################

phrase = input("What phrase do you want to encrypt? ").upper()
rotation = int(input("How many rotations to use? "))

newLetter = ""
newPhrase = ""

for letter in phrase:
    if(letter == " "):
        newLetter = " "
    else:
        newLetter = chr(ord(letter) + rotation)
        if(ord(newLetter) > 90):
            newLetter = chr(ord(newLetter) - 26)

    newPhrase += newLetter

print(newPhrase)

# Now decrypt
phrase = input("What phrase do you want to decrypt? ").upper()
rotation = int(input("How many rotations to use? "))

newLetter = ""
newPhrase = ""

for letter in phrase:
    if(letter == " "):
        newPhrase += " "
        continue
    else:
        newLetter = chr(ord(letter) - rotation)
        if(ord(newLetter) < 65):
            newLetter = chr(ord(newLetter) + 26)

    newPhrase += newLetter

print(newPhrase)

## Method from lab 08b
# ######################################
# # Encrypt plaintext using a Caesar Cipher based on a given rotation and then decrypt
# ######################################
#
# #Create variable for user given numeric entry
# plaintext = ""
# #Alphabet mapping variable
# values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # Create variable to parse plaintext
# encryptLetter = ""
# encryptWord = ""
#
# # Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
# # while(not(number.isnumeric())):
# plaintext = input("What is the plaintext? ").upper()
# rotation = input("How many rotations do you want? ")
#
# # Convert rotation input to int
# rotateTo = int(rotation)
#
# for letter in plaintext:
#     if(letter == " "):
#         encryptWord += " "
#     else:
#         encryptLetter = values[(values.find(letter) + rotateTo) % 26]
#         encryptWord += encryptLetter
#
# print(encryptWord)
#
# ######################################
# # Decrypt plaintext using a Caesar Cipher based on a given rotation
# ######################################
#
# #Create variable for user given numeric entry
# cipher = ""
# #Alphabet mapping variable
# values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # Create variable to parse plaintext
# decryptLetter = ""
# decryptWord = ""
#
# # Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
# # while(not(number.isnumeric())):
# cipher = input("What is the cipher? ").upper()
# rotation = input("How many rotations where there? ")
#
# # Convert rotation input to int
# rotateTo = int(rotation)
#
# for letter in cipher:
#     if(letter == " "):
#         decryptWord += " "
#     else:
#         decryptLetter = values[(values.find(letter) - rotateTo) % 26]
#         decryptWord += decryptLetter
#
# print(decryptWord)

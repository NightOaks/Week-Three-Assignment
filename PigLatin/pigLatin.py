__author__ = 'Devin Simoneaux'

# CIS-125
# Pig Latin Converter
#
# The program takes the user's input and turns it into Pig Latin.

# Variables
pgword = ""
word = ""
vowels = "aeiou"
cvowels = "AEIOU" # I created a separate group of capital vowels so that it will recognize vowels in both cases

# User inputs an English word
word = input("Enter an English word: ")

# Conversion to Pig Latin
first = word[0]
wordlength = len(word)

if first in vowels or first in cvowels: # The or statement checks the first letter of the word against lowercase and uppercase vowels
    pgword = word + "yay"
else:
    pgword = word[1:wordlength] + first + "ay"

#Output the Pig Latin version of the word
print(pgword)
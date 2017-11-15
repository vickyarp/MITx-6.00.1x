# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:08:54 2017

@author: user
"""
#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc

maxChar=''
currentChar=''
previousChar=''
for char in s:
    if char >= previousChar:
        currentChar = currentChar + char
        if len(currentChar) > len(maxChar):
            maxChar = currentChar
    else:
        currentChar = char
    previousChar = char
print (maxChar)
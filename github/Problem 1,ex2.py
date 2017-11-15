# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:00:27 2017

@author: user
"""
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2

numBOB=0
for i in range(len(s)):
    if s[i:i+3]=="bob":
        numBOB+=1
print("Number of times bob occurs is:",numBOB)
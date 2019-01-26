# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:15:34 2019

@author: Zhe Shen
"""

#Given an array of integers, find the first missing positive integer in linear time 
#and constant space. In other words, find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#
#For example, the input [3, 4, -1, 1] should give 2. 
#The input [1, 2, 0] should give 3.
#
#You can modify the input array in-place.
testArr1 = [3, 4, -1 ,1]
resArr1 = 2
#testArr1.sort()
#print(testArr1)
testArr2 = [1 ,2 ,0]
resArr2 = 3

#using sort
def findFirstMissingInt(arr):
    sortedArr = arr
    sortedArr.sort()
    lowestInt = sortedArr[0]
    i = 0
    while(i < len(sortedArr)):
        if (sortedArr[i]+1 in arr or sortedArr[i]+1  == 0):
            i = i + 1
            lowestInt = sortedArr[i]
        else:
            return lowestInt+1

print(findFirstMissingInt(testArr1))
print("\n")
print(findFirstMissingInt(testArr2))
# Problem: Not a subset sum 
# Difficulty: Medium 
# Date: 16 May 2026 
# Language: Python

""" Problem: Given an array of positive integers, find the smallest
positive integer that cannot be represented as the sum
of elements of any subset of the array. """

class Solution:
    def findSmallest(self, arr):
        # code here
        arr.sort()
        res=1
        for i in arr:
            if i>res:
                break
            res+=i
        return res

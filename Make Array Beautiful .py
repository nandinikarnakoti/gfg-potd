# Problem: Make Array Beautiful 
# Difficulty: Easy 
# Date: 17 May 2026

""" 
Problem:
Given an array of negative and non-negative integers,
remove adjacent elements having different signs until
the array becomes beautiful.

A beautiful array contains adjacent integers that are either both positive or both negative.

Note:
0 is considered positive. 
"""
class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        res=[]
        for i in arr:
            if res and ((res[-1]>=0 and i<0) or (res[-1]<0 and i>=0)):
                res.pop()
            else:
                res.append(i)
        return res

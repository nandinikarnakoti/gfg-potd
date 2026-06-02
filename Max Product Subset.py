# Problem: Max Product Subset 
# Difficulty: Medium
# Date: 1 June 2026

""" 
Problem:
Given an array, find the maximum product possible
from any subset of the array.
Return the result modulo 10^9 + 7. 
"""

# ---------------------------------------------------
# Approach: Greedy Product Calculation 
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def findMaxProduct(self, arr):
        # code here
        mod=10**9+7
        if len(arr)==1:
            return arr[0]
        prod=1
        neg_count=0
        zero_count=0
        max_negative=-10**9
        for x in arr:
            if x==0:
                zero_count+=1
                continue
            if x<0:
                neg_count+=1
                max_negative=max(max_negative,x)
            prod*=x
        if zero_count==len(arr):
            return 0
        if neg_count==1 and zero_count+neg_count==len(arr):
            return 0
        if neg_count%2==1:
            prod//=max_negative
        return prod%mod

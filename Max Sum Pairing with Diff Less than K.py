# Problem: Max Sum Pairing with Diff Less than K 
# Difficulty: Easy
# Date: 2 June 2026

""" 
Problem:
Given an array and an integer k, form disjoint pairs
such that the difference between paired elements is
less than k. 

Return the maximum possible sum of all paired elements. 
"""
# --------------------------------------------------- 
# Approach: Greedy Pairing After Sorting 
# Time Complexity: O(N log N) 
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort()
        res=0
        i=len(arr)-1
        while i>0:
            if arr[i]-arr[i-1]<k:
                res+=arr[i]+arr[i-1]
                i-=2
            else:
                i-=1
        return res
        
        

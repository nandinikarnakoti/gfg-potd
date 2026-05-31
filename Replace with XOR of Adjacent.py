# Problem: Replace with XOR of Adjacent 
# Difficulty: Easy 
# Date: 30 May 2026

""" 
Problem:
Modify the array such that every element becomes
the XOR of its adjacent elements.

For first element: 
arr[0] = arr[0] ^ arr[1] 

For last element:
arr[n-1] = arr[n-2] ^ arr[n-1]

For middle elements: 
arr[i] = arr[i-1] ^ arr[i+1]
"""
# --------------------------------------------------- 
# Approach: Temporary Array Simulation 
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def replaceElements(self, arr):
        # code here
        res=[]
        n=len(arr)
        v1=arr[0]^arr[1]
        res.append(v1)
        for i in range(1,n-1):
            curr=arr[i-1]^arr[i+1]
            res.append(curr)
        v2=arr[n-2]^arr[n-1]
        res.append(v2)
        arr[:]=res

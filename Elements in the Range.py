# Problem: Elements in the Range 
# Difficulty: Basic 
# Date: 25 May 2026

""" 
Problem:
Given an array of distinct positive integers and a range
[start, end], determine whether all elements within the
inclusive range are present in the array.

Return true if all elements exist, otherwise false.
"""

# --------------------------------------------------- 
# Approach: Direct Membership Check 
# Time Complexity: O((end - start + 1) * N) 
# Space Complexity: O(1) 
# ---------------------------------------------------
class Solution:
    def checkElements(self, start, end, arr):
        # code here
        for i in range(start,end+1):
            if i not in arr:
                return False
        return True

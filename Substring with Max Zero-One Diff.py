# Problem: Substring with Max Zero-One Diff 
# Difficulty: Medium 
# Date: 4 June 2026

"""
Problem:
Given a binary string, find the maximum value of:
(number of 0s - number of 1s)
among all possible substrings.
If the string contains only 1s, return -1. 
"""

# --------------------------------------------------- 
# Approach: Kadane's Algorithm
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
	def maxSubstring(self, s):
		# code here
        curr = 0
        res = -1
        for i in s:
            val = 1 if i == '0' else -1
            curr = max(val, curr + val)
            res = max(res, curr)
        return res

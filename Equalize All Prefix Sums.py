# Problem: Equalize All Prefix Sums
# Difficulty: Medium 
# Date: 19 June 2026

"""
Problem:
For every prefix arr[0...i], find the minimum
number of operations required to make all elements
in that prefix equal.

One operation increases or decreases an element by 1. 
"""

# --------------------------------------------------- 
# Approach: Median + Prefix Sum
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def optimalArray(self, arr):
        # code here
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
        ans = []
        for i in range(n):
            m = i // 2
            left = arr[m] * (m + 1) - pref[m + 1]
            right = (pref[i + 1] - pref[m + 1]) - arr[m] * (i - m)
            ans.append(left + right)
        return ans
        

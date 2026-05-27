# Problem: Minimum Toggle to Partition 
# Difficulty: Easy 
# Date: 26 May 2026

""" 
Problem: 
Given a binary array containing only 0s and 1s,
find the minimum toggles required so that the
array becomes partitioned:

All 0s appear first, followed by all 1s. 
"""

# ---------------------------------------------------
# Approach: Dynamic Flip Counting 
# Time Complexity: O(N) 
# Space Complexity: O(1)
# ---------------------------------------------------
class Solution:
    def minToggle(self, arr):
        # code here
        ones = 0
        flips = 0
        for i in arr:
            if i == 1:
                ones += 1
            else:
                flips += 1
            flips = min(flips, ones)
        return flips

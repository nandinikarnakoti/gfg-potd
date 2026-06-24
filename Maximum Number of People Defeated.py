# Problem: Maximum Number of People Defeated 
# Difficulty: Medium 
# Date: 23 June 2026

""" 
Problem:
The i-th person has strength i². 

A person can be defeated only if the current
strength p is at least i², after which p decreases
by i². 

Find the maximum number of people that can be defeated. 
"""

# --------------------------------------------------- 
# Approach: Binary Search on Answer 
# Time Complexity: O(log P) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def maxPeopleDefeated(self, p):
        # code here
        low, high = 0, 10000
        while low <= high:
            mid = (low + high) // 2
            total = mid * (mid + 1) * (2 * mid + 1) // 6
            if total <= p:
                low = mid + 1
            else:
                high = mid - 1
        return high

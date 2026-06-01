# Problem: Express as Consecutive Number Sum 
# Difficulty: Easy 
# Date: 31 May 2026

""" 
Problem:
Given a number n, determine whether it can be 
expressed as the sum of two or more consecutive
positive integers. 
"""

# --------------------------------------------------- 
# Approach: Mathematical Observation
# Time Complexity: O(1)
# Space Complexity: O(1) 
# --------------------------------------------------- 

class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        if n&(n-1)==0:
            return False
        return True

# Problem: Last Digit of a^b 
# Difficulty: Medium 
# Date: 20 June 2026

"""
Problem:
Given two very large integers a and b as strings, 
find the last digit of a^b. 
"""
# --------------------------------------------------- 
# Approach: Modular Exponentiation 
# Time Complexity: O(log b) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def getLastDigit(self, a, b):
        # code here
        if b=="0":
            return 1
        return pow(int(a[-1]),int(b),10)
        

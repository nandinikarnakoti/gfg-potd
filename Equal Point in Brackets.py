# Problem: Equal Point in Brackets 
# Difficulty: Easy 
# Date: 11 June 2026

""" 
Problem:
Find the first position k such that:
Number of '(' before k 
=
Number of ')' from k to end.
Return the first such position.
"""

# --------------------------------------------------- 
# Approach: Prefix Open Count + Suffix Close Count 
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def findIndex(self, s):
        # code here 
        close_right = s.count(')')
        open_left = 0
        for i in range(len(s) + 1):
            if open_left == close_right:
                return i
            if i < len(s):
                if s[i] == '(':
                    open_left += 1
                else:
                    close_right -= 1

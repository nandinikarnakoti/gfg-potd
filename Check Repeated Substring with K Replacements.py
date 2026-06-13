# Problem: Check Repeated Substring with K Replacements
# Difficulty: Medium
# Date: 13 June 2026

""" 
Problem:
Given a string s and an integer k.
In one operation, you may replace any substring of 
length k starting at an index i such that i % k == 0. 

Determine whether it is possible to make the entire
string consist of repetitions of a single substring
of length k using at most one replacement.
"""

# --------------------------------------------------- 
# Approach: Frequency Count of K-Length Blocks
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        # code here
        from collections import Counter
        n = len(s)
        if n % k != 0:
            return False
        blocks = [s[i:i+k] for i in range(0, n, k)]
        freq = Counter(blocks)
        if len(freq) == 1:
            return True
        if len(freq) == 2:
            return 1 in freq.values()
        return False
        

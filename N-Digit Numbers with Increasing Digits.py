# Problem: N-Digit Numbers with Increasing Digits 
# Difficulty: Medium 
# Date: 24 June 2026

""" 
Problem:
Generate all n-digit numbers whose digits are 
strictly increasing from left to right. 

Examples: 
12, 159, 6789 
"""

# --------------------------------------------------- 
# Approach: Backtracking (DFS) 
# Time Complexity: O(C(9, n)) 
# Space Complexity: O(n) 
# ---------------------------------------------------

class Solution:
    def increasingNumbers(self, n):
        # code here
        if n == 1:
            return [i for i in range(10)]
        if n > 9:
            return []
        ans = []
        def dfs(length, last_digit, num):
            if length == n:
                ans.append(num)
                return
            for d in range(last_digit + 1, 10):
                dfs(length + 1, d, num * 10 + d)
        for d in range(1, 10):
            dfs(1, d, d)
        return ans

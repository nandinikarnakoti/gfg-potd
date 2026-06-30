# Problem: Max Dot Product with 0 Insertions 
# Difficulty: Medium 
# Date: 29 June 2026

""" 
Problem:
Insert zeros into array b so that its length
becomes equal to a and the dot product is maximized. 
"""
# --------------------------------------------------- 
# Approach: Dynamic Programming
# Time Complexity: O(N × M) 
# Space Complexity: O(N × M) 
# ---------------------------------------------------

class Solution:
    def maxDotProduct(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        NEG = float('-inf')
        dp = [[NEG] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                dp[i][j] = max(
                    dp[i - 1][j],  
                    dp[i - 1][j - 1] + a[i - 1] * b[j - 1]
                )
        return dp[n][m]

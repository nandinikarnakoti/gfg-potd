# Problem: Cut Rope to Maximise Product 
# Difficulty: Medium 
# Date: 17 June 2026

"""
Problem:
Given a rope of length n, cut it into at least
two parts such that the product of the lengths
is maximized.

Return the maximum obtainable product.
"""
# --------------------------------------------------- 
# Approach: Dynamic Programming 
# Time Complexity: O(N²) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def maxProduct(self, n):
        # code here
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(
                    dp[i],
                    j * (i - j),
                    j * dp[i - j]
                )
        return dp[n]
        
        

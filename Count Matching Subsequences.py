# Problem: Count Matching Subsequences 
# Difficulty: Medium 
# Date: 26 June 2026

""" 
Problem:
Count the number of subsequences of s1
that are equal to s2. 

Return the answer modulo 10^9 + 7.
"""

# --------------------------------------------------- 
# Approach: 1D Dynamic Programming 
# Time Complexity: O(N × M) 
# Space Complexity: O(M) 
# ---------------------------------------------------

class Solution:
    def countWays(self, s1, s2):
        # code here
        MOD = 10**9 + 7
        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
        return dp[m]
        

# Problem: Binary Strings with Equal Sum of Two Halves 
# Difficulty: Medium 
# Date: 13 June 2026 

""" 
Problem:
Given n, count all binary strings of length 2n
such that the sum of the first n bits is equal
to the sum of the last n bits. 

Return the answer modulo 10^9 + 7.
"""

# --------------------------------------------------- 
# Approach: Central Binomial Coefficient 
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
    def computeValue(self, n):
        # code here
        MOD = 10**9 + 7
        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact_n = pow(fact[n], MOD - 2, MOD)
        return fact[2 * n] * inv_fact_n % MOD * inv_fact_n % MOD

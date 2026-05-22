# Problem: Check if All Bits Set 
# Difficulty: Basic 
# Date: 21 May 2026

""" 
Problem:
Given a number n, check whether all bits in its 
binary representation are set or not.
Return true if all bits are set, otherwise false.
"""

# --------------------------------------------------- 
# Approach 1: Using Binary Conversion 
# Time Complexity: O(log N)
# Space Complexity: O(log N) 
# ---------------------------------------------------
class Solution:
    def isBitSet(self, n):
        # code here
        val=bin(n)[2:]
        for i in val:
            if i=='0':
                return False
        return True

# ---------------------------------------------------
# Approach 2: Bit Manipulation 
# Time Complexity: O(1)
# Space Complexity: O(1)
# --------------------------------------------------- 
class Solution:
  def isBitSet(self, n):
    if n == 0:
      return False
    return (n & (n + 1)) == 0

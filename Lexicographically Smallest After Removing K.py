# Problem: Lexicographically Smallest After Removing K 
# Difficulty: Medium 
# Date: 5 June 2026

""" 
Problem: 
Given a string s and an integer k, first correct k: 

1. If len(s) is a power of 2, k = k // 2 
2. Otherwise, k = k * 2 
Remove exactly k characters to obtain the
lexicographically smallest possible string.

Return -1 if removal is not possible or if the
resulting string is empty.
"""
# ---------------------------------------------------
# Approach: Monotonic Stack 
# Time Complexity: O(N) 
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def lexicographicallySmallest(self, s, k):
        # code here 
        n = len(s)
        if n & (n - 1) == 0:
            k //= 2
        else:
            k *= 2
        if k >= n:
            return "-1"
        stack = []
        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        while k > 0:
            stack.pop()
            k -= 1
        ans = "".join(stack)
        return ans if ans else "-1"
        

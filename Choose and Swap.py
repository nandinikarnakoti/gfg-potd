# Problem: Choose and Swap 
# Difficulty: Medium 
# Date: 21 June 2026

""" 
Problem:
You may swap all occurrences of any two distinct
characters at most once.

Return the lexicographically smallest string
possible after the operation. 
"""

# --------------------------------------------------- 
# Approach: Greedy Character Swap 
# Time Complexity: O(26 * N)
# Space Complexity: O(26) 
# ---------------------------------------------------

class Solution:
    def chooseSwap(self, s):
        # code here
        present = set(s)
        for ch in s:
            present.discard(ch)
            smaller = None
            for c in map(chr, range(ord('a'), ord(ch))):
                if c in present:
                    smaller = c
                    break
            if smaller:
                res = []
                for x in s:
                    if x == ch:
                        res.append(smaller)
                    elif x == smaller:
                        res.append(ch)
                    else:
                        res.append(x)
                ans = ''.join(res)
                return ans if ans < s else s
        return s

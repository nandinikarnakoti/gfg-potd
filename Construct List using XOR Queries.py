# Problem: Construct List using XOR Queries 
# Difficulty: Medium 
# Date: 17 June 2026

# --------------------------------------------------- 
# Approach: Lazy XOR 
# Time Complexity: O(Q log Q) 
# Space Complexity: O(Q) 
# ---------------------------------------------------

""" 
Problem:
Initially the array contains only [0].

Queries: 
0 x -> Insert x into the array.
1 x -> Replace every element a with a ^ x. 
Return the final array in sorted order. 
"""

class Solution:
    def constructList(self, queries):
        # code here
        arr = [0]
        xr = 0
        for typ, x in queries:
            if typ == 0:
                arr.append(x ^ xr)
            else:
                xr ^= x
        return sorted(num ^ xr for num in arr)
        

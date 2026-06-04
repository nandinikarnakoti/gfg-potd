# Problem: Subarray Frequency Count Queries 
# Difficulty: Medium 
# Date: 3 June 2026

"""
Problem:
For each query [l, r, x], find how many times
x occurs in the subarray arr[l...r].
"""
# --------------------------------------------------- 
# Approach: HashMap + Binary Search
# Time Complexity: O(N + Q log N)
# Space Complexity: O(N)
# ---------------------------------------------------

class Solution:
    def freqInRange(self, arr, queries):
        # code here
        from bisect import bisect_left, bisect_right
        from collections import defaultdict
        pos = defaultdict(list)
        for i, val in enumerate(arr):
            pos[val].append(i)
        ans = []
        for l, r, x in queries:
            indices = pos[x]
            count = bisect_right(indices, r) - bisect_left(indices, l)
            ans.append(count)
        return ans

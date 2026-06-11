# Problem: Binary Searchable Count 
# Difficulty: Medium 
# Date: 10 June 2026

""" 
Problem:
Given an array of distinct integers, count the maximum
number of elements that can be found using standard
Binary Search on the unsorted array.
"""

# --------------------------------------------------- 
# Approach: Binary Search Simulation 
# Time Complexity: O(N log N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def binarySearchable(self, arr):
        # code here 
        n = len(arr)
        ans = 0
        for idx in range(n):
            x = arr[idx]
            l, r = 0, n - 1
            ok = True
            while l <= r:
                mid = (l + r) // 2
                if mid == idx:
                    break
                if mid < idx:
                    if arr[mid] > x:
                        ok = False
                        break
                    l = mid + 1
                else:
                    if arr[mid] < x:
                        ok = False
                        break
                    r = mid - 1
            if ok:
                ans += 1
        return ans

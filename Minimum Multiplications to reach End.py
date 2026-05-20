# Problem: Minimum Multiplications to Reach End 
# Difficulty: Medium 
# Date: 19 April 2026 

""" 
Problem:
Given a start value and an end value, in one operation 
you can multiply the current value by any element from
the array and take modulo 1000.

Return the minimum number of steps required to reach
the end value. If not possible, return -1. 
"""
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        from collections import deque
        q = deque()
        q.append((start, 0))
        vis = [False] * 1000
        vis[start] = True
        while q:
            num, steps = q.popleft()
            if num == end:
                return steps
            for i in arr:
                new = (num * i) % 1000
                if not vis[new]:
                    vis[new] = True
                    q.append((new, steps + 1))
        return -1

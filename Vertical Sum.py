# Problem: Vertical Sum 
# Difficulty: Medium 
# Date: 28 May 2026 

""" 
Problem:
Given a binary tree, find the vertical sum of nodes 
lying in the same vertical line.

Return the sums from the left-most vertical line
to the right-most vertical line. 
"""
# --------------------------------------------------- 
# Approach: DFS + Horizontal Distance Mapping 
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------
# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

class Solution:
    def verticalSum(self, root):
        # code here
        from collections import defaultdict
        res = defaultdict(int)
        def dfs(node, head):
            if not node:
                return
            res[head] += node.data
            dfs(node.left, head - 1)
            dfs(node.right, head + 1)
        dfs(root, 0)
        ans = []
        for i in sorted(res):
            ans.append(res[i])
        return ans

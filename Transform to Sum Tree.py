# Problem: Transform to Sum Tree 
# Difficulty: Easy 
# Date: 24 May 2026 

"""
Problem: Convert a binary tree into a Sum Tree where each node
contains the sum of values present in its left and
right subtrees in the original tree.

Leaf nodes should be converted to 0.
"""

''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def solve(node):
            if not node:
                return 0
            val=node.data
            left_val=solve(node.left)
            right_val=solve(node.right)
            node.data=left_val+right_val
            return val+node.data
        solve(root)
            
            

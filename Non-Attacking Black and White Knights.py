# Problem: Non-Attacking Black and White Knights 
# Difficulty: Medium 
# Date: 6 June 2026

""" 
Problem:
Given an n x m chessboard, find the number of ways
to place one black knight and one white knight such
that they cannot attack each other.

The knights must be placed on different squares.
"""
# --------------------------------------------------- 
# Approach: Simulation 
# Time Complexity: O(N * M) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        total = n * m * (n * m - 1)
        moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)
        ]
        attack = 0
        for i in range(n):
            for j in range(m):
                for dx, dy in moves:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        attack += 1
        return total - attack

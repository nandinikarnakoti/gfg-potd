# Problem: Coverage of all Zeros in a Binary Matrix 
# Difficulty: Easy 
# Date: 18 June 2026

""" 
Problem:
For every 0 cell, count the number of directions
(left, right, up, down) that contain at least one
1 before reaching the matrix boundary. 

Return the total coverage of all 0 cells. 
"""
# ---------------------------------------------------
# Approach: Directional Scan
# Time Complexity: O(N * M * (N + M)) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def findCoverage(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    for c in range(j - 1, -1, -1):
                        if mat[i][c] == 1:
                            ans += 1
                            break
                    for c in range(j + 1, m):
                        if mat[i][c] == 1:
                            ans += 1
                            break
                    for r in range(i - 1, -1, -1):
                        if mat[r][j] == 1:
                            ans += 1
                            break
                    for r in range(i + 1, n):
                        if mat[r][j] == 1:
                            ans += 1
                            break
        return ans
        

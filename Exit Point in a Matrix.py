# Problem: Exit Point in a Matrix 
# Difficulty: Medium 
# Date: 14 June 2026

"""
Problem:
Starting from (0, 0) facing right: 
- If current cell is 0, move in the same direction.
- If current cell is 1:
    * Turn right (clockwise) 
    * Change the cell value to 0

Find the cell from which we exit the matrix. 
"""

# --------------------------------------------------- 
# Approach: Matrix Simulation
# Time Complexity: O(N * M) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def exitPoint(self, mat):
        # code here
        n, m = len(mat), len(mat[0])
        i = j = 0
        d = 0
        while 0 <= i < n and 0 <= j < m:
            if mat[i][j] == 1:
                d = (d + 1) % 4
                mat[i][j] = 0
            if d == 0:
                j += 1
            elif d == 1:
                i += 1
            elif d == 2:
                j -= 1
            else:
                i -= 1
        if i < 0:
            i += 1
        elif i >= n:
            i -= 1
        elif j < 0:
            j += 1
        else:
            j -= 1
        return [i,j]

        

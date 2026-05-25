# Problem: Last Coin in a Game of Alternates 
# Difficulty: Basic 
# Date: 1 May 2026 
""" 
Problem:
Two players alternately pick coins from either end
of the array using a greedy strategy.

At every turn, the player picks the maximum coin
among the two available ends.

Return the value of the last remaining coin. """

# --------------------------------------------------- 
# Approach: Two Pointers 
# Time Complexity: O(N) 
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def coin(self, arr):
        # code here
        l,r=0,len(arr)-1
        while l<r:
            if arr[l]>=arr[r]:
                l+=1
            else:
                r-=1
        return arr[l]

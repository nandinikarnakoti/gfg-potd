# Problem: Seating Arrangement 
# Difficulty: Easy 
# Date: 9 June 2026

"""
Problem:
Given a seating arrangement represented by 0s and 1s,
determine whether k new people can be seated such that
no two occupied seats are adjacent.

If the initial arrangement already contains adjacent
occupied seats, return False.
"""

# --------------------------------------------------- 
# Approach: Greedy Seat Placement 
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        n = len(seats)
        for i in range(n - 1):
            if seats[i] == 1 and seats[i + 1] == 1:
                return False
        count = 0
        for i in range(n):
            if seats[i] == 0:
                left = (i == 0 or seats[i - 1] == 0)
                right = (i == n - 1 or seats[i + 1] == 0)
                if left and right:
                    seats[i] = 1
                    count += 1
        return count >= k

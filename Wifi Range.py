# Problem: Wifi Range 
# Difficulty: Easy 
# Date: 27 May 2026

""" 
Problem:
Given a binary string representing rooms with and without
WiFi routers, determine whether all rooms are covered. Each router covers x rooms to its left and right.
Return true if every room has WiFi coverage. 
"""

# ---------------------------------------------------
# Approach: Interval Coverage 
# Time Complexity: O(N) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def wifiRange(self, s, x):
        # code here
        cover=0
        n=len(s)
        for i in range(n):
            if s[i]=='1':
                left=max(0,i-x)
                right=min(n-1,i+x)
                if left>cover:
                    return False
                cover=max(cover,right+1)
        return cover>=n
                

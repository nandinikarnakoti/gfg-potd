# Problem: Maximum Area Between Bars 
# Difficulty: Medium 
# Date: 22 June 2026

""" 
Problem:
Given the heights of bars arranged in a row,
select any two bars to form a rectangle.

Area = min(height[i], height[j]) × (j - i - 1)
Find the maximum possible area.
"""

# ---------------------------------------------------
# Approach: Two Pointers 
# Time Complexity: O(N) 
# Space Complexity: O(1)
# ---------------------------------------------------

class Solution:
    def maxArea(self, height):
        # code here
        l=0
        r=len(height)-1
        ans=0
        while l<r:
            ans=max(ans,min(height[l],height[r])*(r-l-1))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans

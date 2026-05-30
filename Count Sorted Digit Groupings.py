# Problem: Count Sorted Digit Groupings
# Difficulty: Medium 
# Date: 29 May 2026

"""
Problem:
Given a string of digits, split it into contiguous
substrings such that the sums of digits of the
substrings form a non-decreasing sequence.

Return the total number of valid groupings. """

# --------------------------------------------------- 
# Approach: Recursion + Memoization
# Time Complexity: O(N * SUM * N) 
# Space Complexity: O(N * SUM) 
# ---------------------------------------------------

class Solution:
    def validGroups(self, s):
        # code here
        n=len(s)
        dp={}
        def dfs(i,prev_sum):
            if i==n:
                return 1
            if (i,prev_sum) in dp:
                return dp[(i,prev_sum)]
            ans=0
            curr_sum=0
            for j in range(i,n):
                curr_sum+=int(s[j])
                if curr_sum>=prev_sum:
                    ans+=dfs(j+1,curr_sum)
            dp[(i,prev_sum)]=ans
            return ans
        return dfs(0,0)

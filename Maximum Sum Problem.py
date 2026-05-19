# Problem: Maximum Sum Problem 
# Difficulty: Easy 
# Date: 18 May 2026

""" Problem: Given a number n, break it into three parts:
n/2, n/3, and n/4 recursively. 

At every step, choose the maximum between: 
1. The current number n 
2. The sum obtained after recursive breaks 
Return the maximum possible sum. """

class Solution:
    def maxSum(self, n):
        # code here
        if n==0:
            return 0
        return max(n,self.maxSum(n//2)+self.maxSum(n//3)+self.maxSum(n//4))

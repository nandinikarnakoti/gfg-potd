# Problem: Finding Profession 
# Difficulty: Medium 
# Date: 7 June 2026

""" 
Problem: 
A family tree starts with an Engineer.
Engineer -> (Engineer, Doctor) 
Doctor -> (Doctor, Engineer)

Given the level and position of a person,
determine whether the person is an Engineer
or a Doctor.
"""

# --------------------------------------------------- 
# Approach: Count Bit Flips 
# Time Complexity: O(log pos) 
# Space Complexity: O(1) 
# ---------------------------------------------------

class Solution:
    def profession(self, level, pos):
        # code here
        flips=bin(pos-1).count('1')
        if flips%2==0:
            return "Engineer"
        else:
            return "Doctor"

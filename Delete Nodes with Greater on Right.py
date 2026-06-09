# Problem: Delete Nodes with Greater on Right 
# Difficulty: Easy 
# Date: 16 May 2026

""" 
Problem: 
Given a singly linked list, remove all nodes that
have a node with a greater value somewhere on
their right side.

Return the head of the modified linked list. 
"""

# --------------------------------------------------- 
# Approach: Reverse + Track Maximum 
# Time Complexity: O(N) 
# Space Complexity: O(1)
# ---------------------------------------------------

'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def compute(self,head):
        # code here
        if not head or not head.next:
            return head
        head = self.reverse(head)
        max_so_far = head.data
        curr = head
        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.data
        return self.reverse(head)

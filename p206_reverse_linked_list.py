Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 
            
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        prev = None
        
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
        return prev    #do not forget to return the new head reference at the end!

    #tc: O(n) SC:O(1)
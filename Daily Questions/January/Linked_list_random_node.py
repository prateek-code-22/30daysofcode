
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head):
        self.head = head
        
    def getRandom(self) -> int:
        n, k = 1, 1

        head = self.head
        res =  self.head
        
        while head.next is not None:
            n += 1
            head = head.next
            if random.random() < k/n:
                res = res.next
                k += 1
                
        return res.val
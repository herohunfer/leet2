# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# better
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False



# mine
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1 = p2 = head
        while p1.next and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        tail = list2
        temp = list1
        while tail.next:
            tail = tail.next
        count = 1
        while head:
            if count == a:
                temp = head
            if count == b+1:
                temp.next = list2
                tail.next = head.next
                break
            head = head.next
            count += 1


        return list1

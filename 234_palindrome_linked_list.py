# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.res = True
        def helper(node1, node2):
            if node2.next is None:
                if node1.val != node2.val:
                    self.res = False
                return node1.next
            else:
                current = helper(node1, node2.next)
                if current.val != node2.val:
                    self.res = False
                return current.next
        helper(head, head)
        return self.res

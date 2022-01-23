class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeSort(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        return self.merge(head, head, fast)

    def merge(self, head: ListNode, left: ListNode, right: ListNode):
        current = ListNode(0)
        head = current
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left:
            current.next = left
        else:
            current.next = right
        return head.next

if __name__ == "__main__":
    a = ListNode(2, ListNode(4, ListNode(6, ListNode(-3, ListNode(5)))))
    s = Solution()
    sorteda = s.mergeSort(a)
    while sorteda:
        print(sorteda.val)
        sorteda = sorteda.next

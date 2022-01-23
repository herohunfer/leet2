
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# in place solution

class Solution:
    def flatten(self, head):
        if not head:
            return head
        p = head
        while p:
            if not p.child:
                p = p.next
            else:
                temp = p.child
                while temp.next:
                    temp = temp.next
                temp.next = p.next
                if p.next:
                    p.next.prev = temp
                p.next = p.child
                p.next.prev = p
                p.child = None
        return head

# simple using stack

class Solution:

    def print(self, head):
        s = []
        while head:
            s.append(head.val)
        print(s)

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        res = Node(-1)
        temp = res
        while stack:
            node = stack.pop()
            temp.next = Node(node.val)
            temp.next.prev = temp
            temp = temp.next
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        res.next.prev = None
        return res.next

if __name__ == "__main__":
    s = Solution()

    s.print(s.flatten(head))

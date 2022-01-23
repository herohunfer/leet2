class LinkedNode:
    def __init__(self, key=-1, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.head = LinkedNode(-1)
        self.tail = LinkedNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    def print(self):
        temp = self.head.next
        s = ""
        while temp:
            s += str(temp.key) + "->"
            temp = temp.next

        temp = self.tail
        s += "|||"
        while temp != self.head:
            s += str(temp.key) + "<-"
            temp = temp.prev
        print(s)
    def _add(self, node):
        p = self.head.next
        self.head.next = node
        p.prev = node
        node.prev = self.head
        node.next = p
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self._remove(self.m[key])
        node = LinkedNode(key, value)
        self._add(node)
        self.m[key] = node

        if len(self.m) > self.capacity:
            n = self.tail.prev
            self._remove(n)
            del self.m[n.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

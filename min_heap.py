import sys
class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize)
        # self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 0

    def parent(self, pos):
        return (pos-1) // 2
    def leftChild(self, pos):
        return pos * 2+1
    def rightChild(self, pos):
        return pos * 2 + 2
    def isLeaf(self, pos):
        return pos >= self.size // 2 and pos < self.size
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    def minHeapify(self, pos):
        # print(f"current={pos}")
        if not self.isLeaf(pos):
            left = self.leftChild(pos)
            right = self.rightChild(pos)
            # print(f"pos={self.Heap[pos]} left={self.Heap[left]} right={self.Heap[right]} ")
            if self.Heap[pos] > self.Heap[left] or self.Heap[pos] > self.Heap[right]:
                if self.Heap[left] < self.Heap[right]:
                    self.swap(pos, left)
                    self.minHeapify(left)
                else:
                    self.swap(pos, right)
                    self.minHeapify(right)
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        current = self.size-1
        self.Heap[current] = element
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def Print(self):
        print(self.size)
        for i in range(0, self.size//2):
            print(f'i={i} val={self.Heap[i]} left={self.Heap[self.leftChild(i)]} right={self.Heap[self.rightChild(i)]}')

    def minHeap(self):
        for i in range(self.size//2,0,-1):
            self.minHeapify(i)
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size-1]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped
if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.Print()
    for _ in range(minHeap.size):
        # print("-------removing-----")
        pop = minHeap.remove()
        print(f"The Min val is {pop}")
        # print("------printing------")
        # minHeap.Print()

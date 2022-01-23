class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if len(self.heap1) <= len(self.heap2):
            heappush(self.heap1, -heappushpop(self.heap2, -num))
        else:
            heappush(self.heap2, -heappushpop(self.heap1, num))


    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (self.heap1[0]-self.heap2[0]) / 2
        else:
            return self.heap1[0] if len(self.heap1) > len(self.heap2) else -self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

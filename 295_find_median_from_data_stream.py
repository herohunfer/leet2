# https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
# O(logn) for insertion ( potential shift of list), O(1) for median, O(n) for space

# Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):
#
# (1) length of (small, large) == (k, k)
# (2) length of (small, large) == (k, k + 1)
# After adding the number, total (n + 1) numbers, they will become:
#
# (1) length of (small, large) == (k, k + 1)
# (2) length of (small, large) == (k + 1, k + 1)


from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 388 ms









# O(logn + n) = O(n) for insertion ( potential shift of list), O(1) for median, O(n) for space
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []


    def addNum(self, num: int) -> None:
        l, r = 0, len(self.nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if self.nums[mid]  == num:
                self.nums.insert(mid, num)
                return
            elif self.nums[mid] > num:
                r = mid-1
            else:
                l = mid+1
        # print(f"l={l} r={r}")
        self.nums.insert(l, num)

    def findMedian(self) -> float:
        # print(f"nums={self.nums}")
        if len(self.nums) == 0:
            return 0
        if len(self.nums) % 2 == 0:
            return (self.nums[len(self.nums)//2-1] + self.nums[len(self.nums)//2]) / 2
        else:
            return self.nums[len(self.nums)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

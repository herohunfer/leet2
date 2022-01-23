# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# best solution: patience algorithm
# O(nlogn)
# https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
# PATIENCE (n, c1, c2, …, cn)
# INITIALIZE an array of n empty stacks S1, S2, …, Sn.
# FOR i = 1 TO n
# Sj ← binary search to find leftmost stack that fits ci.
# PUSH (Sj, ci).
# pred[ci] ← PEEK (Sj–1).
# RETURN sequence formed by following pointers from top card
# of rightmost nonempty stack.
# null if j = 1
def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size


# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        vals = [1]
        res = 1
        for i in range(1, len(nums)):
            maxVal = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    maxVal = max(maxVal, vals[j] + 1)
            vals.append(maxVal)
            res = max(maxVal, res)
        return res

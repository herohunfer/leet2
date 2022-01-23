
from collections import Counter
def permuteUnique(self, nums):
    def btrack(path, counter):
        if len(path)==len(nums):
            ans.append(path[:])
        for x in counter:  # dont pick duplicates
            if counter[x] > 0:
                path.append(x)
                counter[x] -= 1
                btrack(path, counter)
                path.pop()
                counter[x] += 1
    ans = []
    btrack([], Counter(nums))
    return ans
# class Solution:
#     def permute(self, nums: List[int], index: int, m: set, sol: List[List[int]]):
#         if index == len(nums):
#             numsStr = '/'.join([str(i) for i in nums])
#             if numsStr not in m:
#                 sol.append(nums[:])
#                 m.add(numsStr)
#         for i in range(index, len(nums)):
#             nums[i],nums[index] = nums[index], nums[i]
#             self.permute(nums, index+1, m, sol)
#             nums[i],nums[index] = nums[index], nums[i]
#
#
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         sol = []
#         self.permute(nums, 0, set(), sol)
#         return list(sol)

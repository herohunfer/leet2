# BackTracking


import copy
def swap(l, a, b):
    l[a], l[b] = l[b], l[a]

class Solution:
    def permutation(self, nums: list[int], index: int, sol: list[list[int]]):
        if index == len(nums):
            sol.append(nums[:])
        for i in range(index, len(nums)):
            swap(nums, i, index)
            self.permutation(nums, index+1, sol)
            swap(nums, i, index)
    def permute(self, nums: list[int]) -> list[list[int]]:
        sol = []
        self.permutation(nums, 0, sol)
        return sol

if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums))

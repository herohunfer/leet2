class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(j * (j-1)//2 for i, j in Counter(nums).items() if j > 1)
        

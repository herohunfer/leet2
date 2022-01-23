class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, quick = 0, 0
        while quick < len(nums):
            while quick+1 < len(nums) and nums[quick] == nums[quick+1]:
                quick += 1
            nums[slow] = nums[quick]
            slow += 1
            quick += 1
        return slow

        

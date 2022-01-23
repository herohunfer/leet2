# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1]
# Output: [1,2]
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res= []
        sum = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
            sum += nums[i]
        sum += nums[n-1]
        res.append(res[0]+(1+n)*n//2-sum)
        return res

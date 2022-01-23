# 0/1 knapsack solution, dp
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if (S & 1) == 1:
            return False
        S //= 2
        dp = [False for i in range(S+1)]
        dp[0] = True
        for num in nums:
            for i in range(S, num-1, -1): # be careful for this, i-num cannot less than 0
                dp[i] = dp[i] or dp[i-num]
            # print(dp)
            if dp[S]:
                return True

        return False



class Solution:
    def canPartition(self, nums) -> bool:
        S = sum(nums)
        if S % 2:
            return False
        half = S // 2
        nums.sort(reverse=True)
        if nums[0] == half:
            return True
        if nums[0] > half:
            return False
        print(nums)
        res, res2 = set([nums[0]]), set([nums[0]])
        for i in range(1, len(nums)):
            for j in res:
                val = j+nums[i]
                if val == half:
                    return True
                elif val < half:
                    res2.add(val)
            res = res2.copy()
            print(res)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,5,11,5,2,2,1,1]))

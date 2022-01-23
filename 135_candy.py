def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n

        # initial state: each kid gets one candy
        nums = [1] * n
        # kids on upwards curve get candies
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])

        return sum(nums)


class Solution:
    def candy(self, ratings) -> int:
        res = [1] * len(ratings)
        base = res[0]
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                base += 1
                res[i] = max(base, res[i])
            else:
                base = res[i]
        base = res[-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                base += 1
                res[i] = max(base, res[i])
            else:
                base = res[i]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.candy([29,51,87,87,72,12]))

# similar problem 11. Container with most water
# memory: O(1) speed: O(n)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        score = nums[k]
        left = k-1
        right = k+1
        current = nums[k]

        while left >= 0 or right < len(nums):
            if left < 0 or (right < len(nums) and nums[left] < nums[right]):
                current = min(current, nums[right])
                right += 1
            else:
                current = min(current, nums[left])
                left -= 1
            score = max(score, (right -1 -left)*current)
        return score




# Sheep's solution
# memory: O(n) speed: O(n)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        a = [0]
        score = 0
        for pos in range(1, len(nums)):
            if nums[pos] > nums[a[-1]]:
                a.append(pos)
            else:
                right = pos
                while len(a) > 0 and nums[pos] <= nums[a[-1]]:
                    left = a[-2] if len(a) > 1 else -1

                    if left < k and k < right:
                        score = max(score, (right - left - 1) * nums[a[-1]])
                    a.pop()
                a.append(pos)
            # print(f"a={a} pos={pos} score={score}")
        right = len(nums)
        while len(a) > 0:
            val = 0
            left = a[-2] if len(a) > 1 else -1
            if left < k and k < right:
                val = (right-left-1)*nums[a[-1]]
                score = max(score, val)
            a.pop()
            # print(f"val={val} a={a}")
        return score





# bad solution
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        score = nums[k]
        smallest = [[0 for i in range(len(nums)) ] for j in range(len(nums))]
        for i in range(0, len(nums)):
            smallest[i][i] = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < smallest[i][j-1]:
                    smallest[i][j] = nums[j]
                else:
                    smallest[i][j] = smallest[i][j-1]

                if i<=k and k <= j:
                    score = max(smallest[i][j] *(j-i+1), score)
        return score

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        score = nums[k]
        a = [0]

        for i in range(1, len(nums)):
            print(f"i={i} a[-1]={a[-1]} a={a} score={score}")
            if nums[i] >= nums[a[-1]]:
                a.append(i)
                if i >= k:
                    score = max(score, nums[i])
            else:
                # pop
                while len(a) > 0 and nums[a[-1]] > nums[i]:
                    a.pop()
                if len(a) == 0:
                    a.append(i)
                    if i>=k:
                        score = max(score, nums[i] * (i+1))
                if a[-1] == nums[i]:
                    if  a[-1] <= k and i >= k:
                        score = max(score, nums[i] * (i - a[-1]+1))

        if a[0] <= k:
            score = max(score, nums[a[0]] * (len(nums) - a[0]+1))
        return score

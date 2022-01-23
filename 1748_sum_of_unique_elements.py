def sumOfUnique(self, A):
    return sum(a for a, c in collections.Counter(A).items() if c == 1)





from collections import Counter
class Solution:
    def sumOfUnique(self, nums) -> int:
        c = Counter(nums)
        return sum([i for i in c if c[i]  == 1])

if __name__ == "__main__":
    s = Solution()
    print(s.sumOfUnique([1,2,3,2]))

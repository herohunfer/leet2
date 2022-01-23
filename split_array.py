def splitArraySameAverage(self, A):
    N, S, P = len(A), sum(A), [1]
    for a in A:
        P[1:] = [(p << a) | q for p, q in zip(P, P[1:] + [0])]
    return any(S * n % N == 0 and P[n] & (1 << (S * n // N))
               for n in range(1, N))


def splitArraySameAverage(self, A):
    n,m,total = len(A), n//2+1, sum(A)
    possible = False
    for i in range(m):
        if total*i%n ==0:
            possible = True
            break
    if not possible:
        return False
    sums = [[] for i in range(m+1)]
    for num in A:
        for i in range(m-1, -1, -1):
            for t in  in sums[i-1]:
                sums[i].append(t+num)
    for i in range(m):
        if total*i%n == 0 && sums[i].find(totalSum*i/n):
            return True
    return False




class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        avg = sum(nums)/len(nums)
        nums.sort()
        bucket1, bucket2, cnt1, cnt2 = 0, 0, 0, 0
        for i in range(len(nums)):
            if bucket1 <= bucket2:
                bucket1 += nums[i]
                cnt1 += 1
                if bucket1/cnt1 == avg:
                    return True
            else:
                bucket2 += nums[i]
                cnt2 += 1
                if bucket2/cnt2 == avg:
                    return True
        return False
# class Solution:
#     def splitArraySameAverage(self, nums) -> bool:
#         avg = sum(nums)/len(nums)
#         q = [[0,0,0]]
#         while q:
#             pos, val, cnt = q.pop()
#             print(pos, val, cnt)
#             if cnt and cnt != len(nums) and val/cnt == avg:
#                 return True
#             if pos != len(nums):
#                 q.append([pos+1, val, cnt])
#                 q.append([pos+1, val+nums[pos], cnt+1])
#         return False

if __name__ == "__main__":
    s = Solution()
    print(s.splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))

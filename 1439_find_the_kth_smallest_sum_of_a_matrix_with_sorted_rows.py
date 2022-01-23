from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, mat, k) -> int:
        first = [sum(m[0] for m in mat)]
        first += [0] * len(mat)
        h = [first]
        # print(h)
        cnt = 0
        appear = set()
        while h:
            current = heappop(h)
            cnt += 1
            # print(current)
            if cnt == k:
                return current[0]
            # print(f"current={current}")
            for i in range(len(mat)):
                # print(f"i={i} current[i+1]={current[i+1]}")
                if current[i+1] + 1 >= len(mat[i]):
                    continue
                temp = current[:]
                # print(mat[i][temp[i+1]+1] - mat[i][temp[i+1]])
                temp[0] += mat[i][temp[i+1]+1] - mat[i][temp[i+1]]
                temp[i+1] += 1
                val = ",".join([str(t) for t in temp])
                if val not in appear:
                    heappush(h, temp)
                    appear.add(val)


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest([[1,3,11],[2,4,6]], 9))
    print(s.kthSmallest([[1,10,10],[1,4,5],[2,3,6]], 7))
    print(s.kthSmallest([[1,1,10],[2,2,9]], 7))

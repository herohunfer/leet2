
# bisect

def minWastedSpace(self, A, boxes):
        A.sort()
        res = float('inf')
        for B in boxes:
            B.sort()
            if B[-1] < A[-1]: continue
            cur = i = 0
            for b in B:
                j = bisect.bisect(A, b, i)
                cur += b * (j - i)
                i = j
            res = min(res, cur)
        return (res - sum(A)) % (10**9 + 7) if res < float('inf') else -1

# binary search

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        def helper(packages, S, l, r, box, pos):
            if pos >= len(box):
                return 0
            left, right = l, r
            while left <= right:
                mid = (left + right )//2
                if packages[mid] <= box[pos]:
                    left = mid + 1
                else:
                    right = mid-1
            val = box[pos]*(left-l)
            # print(f"val={val} left={left} right={right} box={box[pos]}")
            return  val+ helper(packages, S, left, r, box, pos+1)

        packages.sort()
        S = sum(packages)
        res = -1
        for box in boxes:
            sorted_box = sorted(box)
            if packages[-1] > sorted_box[-1]:
                continue
            cnt = helper(packages, S, 0, len(packages)-1, sorted_box, 0) - S
            res = min(res, cnt) if res != -1 else cnt
        return res % (10**9+7) if res != -1 else -1

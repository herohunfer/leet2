from heapq import heappush, heappop


# append 0 to heights, and keep -1 in stack in case lowest height
def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans





class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        h = [0]
        res = 0
        for i in range(1, len(heights)):
            while h and heights[i] < heights[h[-1]]:
                current = h.pop()
                res = max(res, heights[current]*(i-(h[-1]+1 if len(h)>0 else 0)))
            h.append(i)
            print(f"res={res} h={h}")
        return res

if __name__ == "__main__":
    s = Solution()
    # print(s.largestRectangleArea([2,1,2]))
    # print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([2,4]))

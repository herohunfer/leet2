from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: heappop(live)
            if negH: heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]






class Solution:
    def getSkyline(self, buildings):
        def binary_search(h, val, l, r):
            while l<=r:
                mid = (l+r)//2
                if h[mid] == val:
                    return mid
                elif h[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        neg = []
        pos = []
        for building in buildings:
            pos.append((building[0], building[2]))
            neg.append((building[1], building[2]))
        pos.sort()
        neg.sort()
        print(f"pos={pos} neg={neg}")
        h = []

        p = 0
        n = 0
        current = 0
        res = {}
        while p < len(pos) or n < len(neg):
            if p < len(pos) and n < len(neg) and pos[p] == neg[n]:
                p += 1
                n += 1
            elif n == len(neg) or (p < len(pos) and pos[p][0] < neg[n][0]):
                if len(h) == 0 or pos[p][1] > h[-1]:
                    current =  max(res[pos[p][0]], pos[p][1]) if pos[p][0] in res else pos[p][1]
                    res[pos[p][0]] = current
                ip = binary_search(h, pos[p][1], 0, len(h)-1)
                h.insert(ip, pos[p][1])
                p += 1
            else:
                ip = binary_search(h, neg[n][1], 0, len(h)-1)
                h.pop(ip)
                if current == abs(neg[n][1]):
                    current = h[-1] if len(h) > 0 else 0
                    if current < abs(neg[n][1]):
                        res[neg[n][0]] =  max(res[neg[n][1]], current) if neg[n][0] in res else current
                n += 1
            # print(f"h={h}, res={res} processed: {point},{val}")
        a = [(i,j) for i,j in res.items()]
        return sorted(a)

if __name__ == "__main__":
    s = Solution()
    print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(s.getSkyline([[0,2,3],[2,5,3]]))

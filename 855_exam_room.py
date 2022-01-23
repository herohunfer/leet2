import sys
class ExamRoom:
    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) / 2 > d:
                    d, res = (b - a) / 2, (b + a) / 2
            if N - 1 - L[-1] > d: res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        self.L.remove(p)



class ExamRoom:

    def __init__(self, n: int):
        self.res = []
        self.n = n

    def seat(self) -> int:
        if not self.res:
            self.res.append(0)
            return 0
        elif len(self.res) == 1:
            if self.n//2 > self.res[0]:
                self.res.append(self.n-1)
                return self.n-1
            else:
                self.res.insert(0, 0)
                return 0

        distance = self.res[0]
        pos = 0
        for i in range(1, len(self.res)):
            current = (self.res[i] - self.res[i-1])//2
            if current > distance or (current == distance and i < pos):
                distance = current
                pos = i
        if self.res[-1] < self.n-1 and self.n-1-self.res[-1] > distance:
            self.res.append(self.n-1)
            return self.n-1
        self.res.insert(pos, self.res[pos-1]+distance if pos > 0 else 0)
        print(self.res)
        return self.res[pos-1]+distance if pos > 0 else 0

    def leave(self, p: int) -> None:
        for i in range(len(self.res)):
            if self.res[i] == p:
                break
        self.res.pop(i)
        print(self.res)
# from heapq import heappush, heappop, heapify
# class ExamRoom:
#
#     def __init__(self, n: int):
#         self.gaps = []
#         self.n = n
#
#
#     def seat(self) -> int:
#         if not self.gaps:
#             self.gaps.append([-self.n+1, 0])
#             return 0
#         elif len(self.gaps) == 1:
#             self.gaps.append([0, self.n-1])
#             return self.n-1
#         current = heappop(self.gaps)
#         pos = current[1] + abs(current[0])//2
#         heappush(self.gaps, [-(-current[0]//2), current[1]])
#         heappush(self.gaps, [-(-current[0]//2), pos])
#
#         print(self.gaps)
#         return pos
#
#     def leave(self, p: int) -> None:
#         # print(self.gaps)
#         for pos in range(len(self.gaps)):
#             if self.gaps[pos][1] == p:
#                 break
#         prev = -1
#         for i in range(len(self.gaps)):
#             if self.gaps[i][1] < self.gaps[pos][1] and (prev == -1 or self.gaps[i][1] > self.gaps[prev][1]):
#                 prev = i
#         # print(f"pos={pos} prev={prev}")
#         self.gaps[prev][0] += self.gaps[pos][0]
#         self.gaps.pop(pos)
#         heapify(self.gaps)
#         # print(self.gaps)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

if __name__ == "__main__":
    # e = ExamRoom(10)
    # print(e.seat())
    # print(e.seat())
    # print(e.seat())
    # print(e.seat())
    # print(e.leave(4))
    # print(e.seat())
    e = ExamRoom(10)
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.leave(0))
    print(e.leave(4))
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.leave(0))
    print(e.leave(4))
    print(e.seat())
    print(e.seat())

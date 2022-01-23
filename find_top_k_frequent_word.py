import heapq
def top_k_frequent(slist: list, k: int):
    m = {}
    for s in slist:
        if s in m:
            m[s] += 1
        else:
            m[s] = 1
    print(m)
    h = []
    for  key,val in m.items():
        print(f'{key} {val}')
        if len(h) < k:
            heapq.heappush(h, (val, key))
        else:
            if h[0][0] < val:
                heapq.heappop(h)
                heapq.heappush(h, (val, key))
    for _ in range(k):
        print(heapq.heappop(h))

if __name__ == "__main__":
    top_k_frequent(['A', 'B', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'A','C', 'D', 'C'],3)

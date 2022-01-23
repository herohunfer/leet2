class Solution:
    def frequencySort(self, s: str) -> str:
        h = []
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for c, val in m.items():
            heappush(h, (-val,c))
        res = ""
        while h:
            val, c = heappop(h)
            res += c*abs(val)
        return res

    def frequencySort(self, s: str) -> str:
        return "".join([i*j for i, j in Counter(s).most_common()])

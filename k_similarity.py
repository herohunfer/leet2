class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        news1 = ""
        news2 = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                news1 += s1[i]
                news2 += s2[i]
        if news1 == "":
            return 0
        print(news1, news2)
        q = [(news2, 0, 0)]
        p = 0
        m = set()
        while p < len(q):
            current, pos, cnt = q[p]
            if news1[pos:] == current:
                print(q)
                return cnt
            pos2 = 0
            while news1[pos] == current[pos2]:
                pos += 1
                pos2 += 1

            for i in range(pos2+1, len(current)):
                if news1[pos] == current[i]:
                    temp = current[pos2+1:i] + current[pos2] + current[i+1:]
                    if temp not in m:
                        q.append((temp, pos+1, cnt+1))
                        m.add(temp)
            p += 1
    # def kSimilarity(self, s1: str, s2: str) -> int:
    #     m = {}
    #     res = 0
    #     for i in range(len(s1)):
    #         if s1[i] != s2[i]:
    #             if s2[i]+s1[i] in m:
    #                 if m[s2[i]+s1[i]] > 1:
    #                     m[s2[i]+s1[i]] -= 1
    #                 else:
    #                     del m[s2[i]+s1[i]]
    #                 res += 1
    #             else:
    #                 m[s1[i]+s2[i]] = m.get(s1[i]+s2[i], 0)+1
    #
    #
    #         print(f"{s1[i]} {s2[i]} {m}")
    #     return res + max(len(m.values())-1, 0)

if __name__ == "__main__":
    s = Solution()
    print(s.kSimilarity("aabbccddee", "dcacbedbae"))

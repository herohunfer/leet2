def findAnagrams(self,s: str, p: str) -> List[int]:
    res = []
    if len(p)> len(s):
        return res
    cnt = {}
    for c in p:
        cnt[c] = cnt.get(c, 0) + 1
    counter = len(cnt)
    begin,end= 0,0
    while end < len(s):
        c = s[end]
        if c in cnt:
            cnt[c]-=1
            if not cnt[c]:
                counter -= 1
        end += 1

        while counter == 0:
            c = s[begin]
            if c in cnt:
                cnt[c] += 1
                if cnt[c] == 1:
                    counter += 1
            if end-begin == len(t):
                res.append(begin)
            begin += 1






class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = [0]*26
        current = 0
        res = []
        if len(p) > len(s):
            return res
        for c in p:
            cnt[ord(c)-ord('a')] += 1
            current += 1
        for i in range(len(p)):
            if cnt[ord(s[i])- ord('a')] > 0:
                current -= 1
            cnt[ord(s[i])- ord('a')] -= 1
        if current == 0:
            res.append(0)
        for i in range(len(p), len(s)):
            if cnt[ord(s[i]) - ord('a')] > 0:
                current -= 1
            cnt[ord(s[i]) - ord('a')] -= 1
            if cnt[ord(s[i-len(p)])-ord('a')] >= 0:
                current += 1
            cnt[ord(s[i-len(p)])-ord('a')] += 1
            if current == 0:
                res.append(i-len(p)+1)
        return res

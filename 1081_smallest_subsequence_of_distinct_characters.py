def smallestSubsequence(self, S):
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)
        
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = [[] for i in range(26)]
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')].append(i)
        current = len(s)
        for i in range(25, -1, -1):
            if len(cnt[i]) > 1:
                temp = cnt[i][-1]
                while cnt[i] and cnt[i][-1] > current:
                    cnt[i].pop()
                if cnt[i]:
                    cnt[i] = [cnt[i][-1]]
                else:
                    cnt[i] = [temp]
                current = min(current, cnt[i][-1])
            elif len(cnt[i]) == 1:
                current = min(current, cnt[i][-1])
        res = [(i, cnt[i][-1]) for i in range(26) if len(cnt[i]) > 0]
        res.sort(key=lambda item: item[1])
        return "".join([chr(ord('a')+item[0]) for item in res])

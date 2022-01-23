class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        maxLen = max(len(word) for word in wordDict)
        res = [[] for _ in range(maxLen)]
        # print(f"maxLen={maxLen}")
        for i in range(len(s)):
            current = []
            for j in range(1, maxLen+1):
                if i-j+1 >= 0 and s[i-j+1:i+1] in wordDict:
                    if i-j+1 == 0:
                        current.append(s[i-j+1:i+1])
                    else:
                        index = maxLen-j
                        prev = res[index]
                        for sol in prev:
                            current.append(sol + " "+ s[i-j+1:i+1])

            res.append(current)
            res.pop(0)
            # print(f"res={res}")
        return res[-1]

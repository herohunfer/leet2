class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [len(s)] * len(s)
        current = len(s)
        for i in range(len(s)):
            if s[i] == c:
                current = 0
                j = i-1
                temp = 1
                while j >= 0 and res[j] > temp:
                    res[j] = temp
                    temp += 1
                    j -= 1

            res[i] = current
            current += 1
        return res
                

class Solution:
    def secondHighest(self, s: str) -> int:
        highest = -1
        second = -1
        for c in s:
            if '0' <= c <= '9':
                if int(c) == highest:
                    continue
                if int(c) > highest:
                    second = highest
                    highest = int(c)
                else:
                    second = max(second, int(c))
        return second

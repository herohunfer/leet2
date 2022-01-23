from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        counter = Counter(t)
        I, J = 0, 0
        i = 0
        for j, c in enumerate(s, 1):
            if counter[c] > 0:
                missing -= 1
            counter[c] -= 1
            if missing == 0:
                while i < j and counter[s[i]] < 0:
                    counter[s[i]] += 1
                    i += 1
                # first i that exceeds the missing limit
                missing += 1
                counter[s[i]] += 1
                if J == 0 or J-I > j-i:
                    I, J = i, j
                i += 1
            # print(f"i={i} j={j} c={c} missing={missing} counter={counter} I={I} J={J}")
        return s[I:J]

       

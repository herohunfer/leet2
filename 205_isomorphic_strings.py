class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        n = set()
        if len(s) != len(t):
            return False
        for a,b in zip(s,t):
            if a in m and m[a] != b:
                return False
            elif a not in m and b in n:
                return False
            elif a not in m:
                m[a] = b
                n.add(b)
        return True

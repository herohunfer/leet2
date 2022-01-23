class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        M = {}
        N = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in M and M[pattern[i]] != s[i]:
                return False
            elif s[i] in N and N[s[i]] != pattern[i]:
                return False
            else:
                M[pattern[i]] = s[i]
                N[s[i]] = pattern[i]
        return True



    # best solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(2, len(s)+1):
            for j in range(0, len(s)- i+1):
                print(f"a={s[j:j+i]}  b={s[j+i:j:-1]}")
                if s[j:j+i] == s[j:j+i][::-1]:
                    res += 1
        return res

if __name__== "__main__":
    s = Solution()
    print(s.countSubstrings("aaa"))

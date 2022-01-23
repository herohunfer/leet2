class Solution:
    def romanToInt(self, s: str) -> int:
        pos = 0
        res = 0
        while pos < len(s):
            if s[pos] == "M":
                res += 1000
            elif s[pos] == "D":
                res += 500
            elif s[pos] == "L":
                res += 50
            elif s[pos] == "V":
                res += 5
            elif s[pos] == "C":
                temp = 0
                while pos < len(s) and s[pos] == "C":
                    pos += 1
                    temp += 100
                if pos < len(s):
                    if s[pos] == "D":
                        res += 500 - temp
                    elif s[pos] == "M":
                        res += 1000 - temp
                    else:
                        res += temp
                        pos -= 1
                else:
                    res += temp
            elif s[pos] == "X":
                temp = 0
                while pos < len(s) and s[pos] == "X":
                    pos += 1
                    temp += 10
                if pos < len(s):
                    if s[pos] == "L":
                        res += 50 - temp
                    elif s[pos] == "C":
                        res += 100 - temp
                    else:
                        res += temp
                        pos -= 1
                else:
                    res += temp
            elif s[pos] == "I":
                temp = 0
                while pos < len(s) and s[pos] == "I":
                    pos += 1
                    temp += 1
                if pos < len(s):
                    if s[pos] == "V":
                        res += 5 - temp
                    elif s[pos] == "X":
                        res += 10 - temp
                    else:
                        res += temp
                        pos -= 1
                else:
                    res += temp
            pos += 1
        return res

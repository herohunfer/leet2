class Solution:
    def restoreIpAddresses(self, s: str):
        self.res = []
        if len(s) > 12:
            return []
        def helper(s, pos, q):
            # print(f"s={s} pos={pos} q={q}")
            if pos == len(s):
                return
            if len(q) == 3:
                if len(s) - pos <= 3 and pos < len(s) and int(s[pos:]) <= 255:
                    if s[pos] == '0' and len(s)-pos > 1:
                        return
                    q.append(s[pos:])
                    self.res.append(".".join(q))
                    q.pop()
                return
            valid = 255

            for i in range(1,4):
                if s[pos] == "0" and i > 1:
                    return
                if pos+i <= len(s) and int(s[pos:pos+i]) <= valid:
                    q.append(s[pos:pos+i])
                    helper(s, pos+i, q)
                    q.pop()
        helper(s, 0, [])
        return self.res


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("0000"))
    print(s.restoreIpAddresses("1111"))
    print(s.restoreIpAddresses("010010"))
    print(s.restoreIpAddresses("101023"))

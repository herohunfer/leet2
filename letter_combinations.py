class Solution:
    def letterCombinations(self, digits: str):
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.res = []
        def helper(digits, stack):
            # print(stack)
            if len(digits) == 0:
                return
            i = len(stack)
            if i == len(digits):
                self.res.append(stack)
                return
            for c in self.mapping[ord(digits[i])-ord('0')]:
                stack += c
                helper(digits, stack)
                stack = stack[:-1]
                # print(f"stack={stack}")
        helper(digits, "")
        return self.res

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(""))
    print(s.letterCombinations("2"))

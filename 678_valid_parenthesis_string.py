# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
# The following rules define a valid string:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for c in s:
            if c == "(":
                cmin += 1
                cmax += 1
            elif c == ")":
                cmax -= 1
                cmin = max(cmin-1, 0)
            else:
                cmax += 1
                cmin = max(cmin-1, 0)
            if cmax < 0:
                return False
        return cmin == 0

# wrong answer for case: *(
class Solution:
    def checkValidString(self, s: str) -> bool:
        pos = 0
        cnt = 0
        star = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
                if star + cnt < 0:
                    return False
            else:
                star += 1
        return cnt == 0 or star >= abs(cnt)

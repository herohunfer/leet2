# better solution with stack, save pervious operand for second number
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)


# mine

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s, left, right):
            pos = left
            num1, num2 = 0,0
            op = ''
            step = 0

            while pos <= right+1:
                if  (pos != right+1) and (ord('0') <= ord(s[pos]) <= ord('9')):
                    if step == 0:
                        num1 = num1*10 + ord(s[pos]) - ord('0')
                    else:
                        num2 = num2*10 + ord(s[pos]) - ord('0')
                else:
                    if step == 1:
                        if op == '*':
                            num1 = num1 * num2
                        elif op == '/':
                            num1 = num1//num2
                        elif op == '+':
                            num1 = num1 + num2
                        elif op == '-':
                            num1 = num1 - num2
                        num2 = 0
                        op = s[pos] if pos < right+1 else ''
                    else:
                        step += 1
                        op = s[pos] if pos < right+1 else ''
                pos += 1
            return num1

        s = "".join([ch for ch in s if ch != " "])
        i = 0
        while i < len(s):
            if s[i] == '*' or s[i] == '/':
                left, right = i-1, i+1
                while left > -1:
                    if ord('0') > ord(s[left]) or ord(s[left]) > ord('9'):
                        break
                    left -= 1
                while right < len(s):
                    if ord('0') > ord(s[right]) or ord(s[right]) > ord('9'):
                        break
                    right += 1
                s = s[:left+1] + str(helper(s, left+1, right-1)) + s[right:]
                i = left+1
            else:
                i += 1
        return helper(s, 0, len(s)-1)

if __name__ == "__main__":
    s = Solution()
    # print(s.calculate("3+2*2"))
    print(s.calculate(" 3/2 "))
    print(s.calculate(" 3+5 / 2 "))

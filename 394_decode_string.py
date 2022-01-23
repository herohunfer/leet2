def stacky(s):
    """
    When we hit an open bracket, we know we have parsed k for the contents of the bracket, so
    push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
    the enclosed string k times.
    """
    stack = []
    current_string = ""
    k = 0

    for char in s:
        if char == "[":
            # Just finished parsing this k, save current string and k for when we pop
            stack.append((current_string, k))
            # Reset current_string and k for this new frame
            current_string = ""
            k = 0
        elif char == "]":
            # We have completed this frame, get the last current_string and k from when the frame
            # opened, which is the k we need to duplicate the current current_string by
            last_string, last_k = stack.pop(-1)
            current_string = last_string + last_k * current_string
        elif char.isdigit():
            k = k * 10 + int(char)
        else:
            current_string += char

    return current_string



class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s, start, end):
            pos = start
            num = 0
            res = ''
            chars = ''
            while pos < end:
                if s[pos] == '[':
                    if chars:
                        res += chars * (num if num else 1)
                        chars = ''
                        num = 0
                    temp = pos
                    cnt = 1
                    pos += 1
                    while cnt and pos < end:
                        if s[pos] == '[':
                            cnt +=1
                        elif s[pos] == ']':
                            cnt -= 1
                        pos += 1
                    current = helper(s, temp+1, pos-1)
                    print(f"current={current} num={num}")
                    res += current * (num if num else 1)
                    num = 0
                elif '0' <= s[pos] <= '9':
                    if chars:
                        res += chars
                        chars = ''
                    num = num*10 + ord(s[pos]) - ord('0')
                    pos += 1
                elif 'a' <= s[pos] <= 'z':
                    chars += s[pos]
                    pos += 1
            if chars:
                res += chars * (num if num else 1)
            return res
        return helper(s, 0, len(s))


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("abc3[cd]xyz"))
    # print(s.decodeString("3[a]2[bc]"))

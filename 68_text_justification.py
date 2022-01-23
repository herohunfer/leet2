def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        q = []
        l = 0
        res = []
        words.append("1"*maxWidth)
        for word in words:
            if not q or (l + len(word) + len(q) <= maxWidth):
                q.append(word)
                l += len(word)
            else:
                if word[0] == "1":
                    remaining = maxWidth - l - len(q) + 1
                    temp = " ".join(q) + " "*remaining
                    res.append(temp)
                else:
                    extra = maxWidth - l
                    remaining = extra % (len(q)-1) if len(q) > 1 else 0
                    each = extra // (len(q)-1) if len(q) > 1 else extra
                    temp = q[0] + " "*(each + (1 if remaining else 0))
                    if remaining > 0:
                        remaining -= 1
                    for w in q[1:-1]:
                        temp += w + " "*(each + (1 if remaining else 0))
                        if remaining > 0:
                            remaining -= 1
                    if len(q) > 1:
                        temp += q[-1]
                    res.append(temp)
                    q = [word]
                    l = len(word)
        return res

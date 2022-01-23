class Solution:
    def spellchecker(self, wordlist, queries):
        m_exact = set(wordlist)
        m = {}
        for word in wordlist:
            if word.lower() not in m:
                m[word.lower()] = word
            current = "".join(['*' if c.lower() in "aeiou" else c.lower() for c in word ])
            if current not in m:
                m[current] = word
        res = []
        print(m)
        for query in queries:
            if query in m_exact:
                res.append(query)
            else:
                q = query.lower()
                if q in m:
                    res.append(m[q])
                else:
                    current = "".join(['*' if c in "aeiou" else c for c in q ])
                    if current in m:
                        res.append(m[current])
                    else:
                        res.append("")
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
    # print(s.spellchecker(["YellOw"], ["yollow"]))

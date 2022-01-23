def uniqueMorseRepresentations(self, words):
    d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        m = set()
        for word in words:
            m.add("".join([s[ord(c)-ord('a')]for c in word]))
        return len(m)

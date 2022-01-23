# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# test cases: 1. aa / ac  2. kcl/kcl   3. bank/kanb 4. abcd / dcba
import sys
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pos = sys.maxsize
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if pos == sys.maxsize:
                    pos = i
                    continue
                val1 = s1[:pos] + s1[i] + s1[pos+1:i] + s1[pos] + s1[i+1:]
                return  val1 == s2
                break
        return pos == sys.maxsize

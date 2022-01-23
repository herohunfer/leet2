class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return 0 if not needle else -1
        if not needle:
            return 0
        for i in range(0, len(haystack)- len(needle)+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

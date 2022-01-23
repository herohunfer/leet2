# O(N) in time O(1) in space
def findSpecialInteger(self, arr: List[int]) -> int:
        gap = len(arr) // 4
        for i in range(len(arr) - gap):
            if arr[i] == arr[i + gap]: return arr[i]
        return arr[-1]


# O(N) in time O(N) in space
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]

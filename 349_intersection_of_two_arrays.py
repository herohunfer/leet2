class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = {}
        for i in nums1:
            if i not in m:
                m[i] = 1
        for i in nums2:
            if i in m and m[i] == 1:
                res.append(i)
                m[i] += 1
        return res

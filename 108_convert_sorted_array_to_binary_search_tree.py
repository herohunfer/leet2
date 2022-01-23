# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, left, right):
            if left > right:
                return None
            middle = (left+right)//2
            mid = TreeNode(nums[middle])
            mid.left = helper(nums, left, middle-1)
            mid.right = helper(nums, middle+1, right)
            return mid

        if not nums:
            return None
        root = helper(nums, 0, len(nums)-1)
        return root

            

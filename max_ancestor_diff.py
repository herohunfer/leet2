# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node):
            if not node:
                return 10001, -1
            left_min, left_max = helper(node.left)
            right_min, right_max = helper(node.right)
            self.res = max(self.res,
                           abs(node.val - left_min) if left_min != 10001 else 0,
                           abs(node.val - left_max) if left_max != -1 else 0,
                           abs(node.val - right_min) if right_min != 10001 else 0,
                           abs(node.val - right_max) if right_max != -1 else 0)
            return min(node.val, left_min, right_min), max(node.val, left_max, right_max)
        helper(root)
        return self.res

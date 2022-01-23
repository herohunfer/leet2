# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# careful for initial value for res, this needs to be negative to cover [-3] case
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def helper(root: TreeNode) -> int:
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, left + right + root.val)
            return max(root.val + max(left, right), 0)


        helper(root)

        return self.res

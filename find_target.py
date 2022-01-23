# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.m = set()
        self.res = False
        def helper(root, k):
            if not root:
                return
            if root.val in self.m:
                self.res = True
                return
            self.m.add(k - root.val)
            helper(root.left, k)
            helper(root.right, k)
        helper(root, k)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def helper(node, p, q):
            if not node:
                return node
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            if (left == p and right == q) or \
               (left == q and right == p) or \
               (node == p and left == q) or \
               (node == p and right == q) or \
               (node == q and left == p) or \
               (node == q and right == p):
                self.res = node
                return node
            else:
                if node == p or node == q:
                    return node
                elif left == p or left == q:
                    return left
                else:
                    return right
        helper(root, p, q)
        return self.res

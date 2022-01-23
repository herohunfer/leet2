# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.res = None
        self.maxDepth = 0
        def helper(node, depth):
            if not node:
                return 0
            if depth > self.maxDepth:
                self.res = node
                self.maxDepth = depth
            left = helper(node.left, depth+1)
            right = helper(node.right, depth+1)
            if left >= self.maxDepth and left == right:
                self.res = node
                self.maxDepth = left
            return max(left, right, depth)
        helper(root, 0)
        return self.res

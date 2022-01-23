# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# key point: return depth and which node causes the deepest, bottom up
 def subtreeWithAllDeepest(self, root):
        def deep(root):
            if not root: return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]: return l[0] + 1, l[1]
            elif l[0] < r[0]: return r[0] + 1, r[1]
            else: return l[0] + 1, root
        return deep(root)[1]




class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.maxDepth = 0
        self.res = None
        def helper(root, depth):
            if root is None:
                return 0
            leftDepth = helper(root.left, depth+1)
            rightDepth = helper(root.right, depth+1)
            maxCurrent = max(leftDepth, rightDepth, depth)
            if maxCurrent > self.maxDepth:
                self.maxDepth = maxCurrent
                self.res = root
            elif leftDepth == rightDepth == self.maxDepth:
                self.res = root
            return maxCurrent
        helper(root, 0)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.nums = []
        def helper(root):
            if not root:
                return
            self.nums.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root1)
        helper(root2)
        return sorted(self.nums)
        

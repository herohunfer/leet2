# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res = []
        current = 0
        q = [root]
        q1 = []
        cnt = 1
        while q:
            while q:
                node = q.pop()
                current += node.val
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            res.append(current/cnt)
            q = q1
            q1 = []
            current = 0
            cnt = len(q)
        return res

            

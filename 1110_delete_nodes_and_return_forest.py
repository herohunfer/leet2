# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    to_delete_set = set(to_delete)
    res = []
    def helper(root, is_root):
        if not root:
            return None
        root_deleted = root.val in to_delete_set

        if is_root and not root_deleted:
            res.append(root)
        root.left = helper(root.left, root_deleted)
        root.right = helper(root.right, root_deleted)
        return None if root_deleted else root
    helper(root, True)
    return res



class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        stack = [root]
        evaluate = {root.val} if root else {}
        res = []
        while stack:
            current = stack.pop()
            if current is None:
                continue
            if current.val in to_delete:
                if current.left:
                    evaluate.add(current.left.val)
                if current.right:
                    evaluate.add(current.right.val)
            elif current.val in evaluate:
                res.append(current)
            stack.append(current.left)
            stack.append(current.right)
            if current.left and current.left.val in to_delete:
                current.left = None
            if current.right and current.right.val in to_delete:
                current.right = None
        return res

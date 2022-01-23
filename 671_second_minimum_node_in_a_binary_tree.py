# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(self, root: TreeNode) -> int:
    self.root_val = root.val
    self.second = float(inf)

    def dfs(node):
        if node:
            if self.root_val < node.val < self.second:
                self.second = node.val
            if self.root_val == node.val:
                dfs(node.left)
                dfs(node.right)
    dfs(root)
    return self.second if self.second!=float('inf') else -1


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def helper(node, minimum):
            if not node:
                return -1
            if node.val != minimum:
                return node.val
            left = helper(node.left, minimum)
            right = helper(node.right, minimum)
            if left != -1 and right != -1:
                return min(left, right)
            elif left != -1:
                return left
            else:
                return right
        if not root:
            return -1
        return helper(root, root.val)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
    print(s.findSecondMinimumValue(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        temp = self.root
        while temp:
            self.stack.append(temp)
            temp = temp.left



    def next(self) -> int:
        current = self.stack.pop()
        if current.right:
            temp = current.right
            while temp:
                self.stack.append(temp)
                temp = temp.left
        return current.val


    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

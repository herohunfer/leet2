import sys
class TreeNode:
    def __init__(self, *args, **kwargs):
        self.val = kwargs.get("val", 0)
        self.left = kwargs.get("left", None)
        self.right = kwargs.get("right", None)


def is_bst(root: TreeNode, min: int, max: int):
    if root is None:
        return True
    if root.val <= min or root.val >= max:
        return False
    return is_bst(root.left, min, root.val) and is_bst(root.right, root.val, max)


if __name__ == "__main__":
    t = TreeNode(val = 10, left = TreeNode(val = 5, left = TreeNode(val = 2), right = TreeNode(val = 7)), right = TreeNode( val = 15, left = TreeNode(val= 12), right = TreeNode(val = 20)))
    print(is_bst(t, - sys.maxsize-1, sys.maxsize))

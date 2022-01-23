import sys
class TreeNode:
    def __init__(self, *args, **kwargs):
        self.val = kwargs.get("val", 0)
        self.left = kwargs.get("left", None)
        self.right = kwargs.get("right", None)

def print_bst_in_range(root: TreeNode, low: int, high: int):
    if root is None:
        return
    if root.val > low:
        print_bst_in_range(root.left, low, high)
    if root.val >= low and root.val <= high:
        print(root.val)

    if root.val < high:
        print_bst_in_range(root.right, low, high)

if __name__ == "__main__":
    t = TreeNode(val = 10, left = TreeNode(val = 5, left = TreeNode(val = 2), right = TreeNode(val = 7)), right = TreeNode( val = 15, left = TreeNode(val= 12), right = TreeNode(val = 20)))
    print_bst_in_range(t, - sys.maxsize-1, sys.maxsize)

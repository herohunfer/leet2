# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# need use BST information
 def deleteNode(root, key):
	if not root: # if root doesn't exist, just return it
		return root
	if root.val > key: # if key value is less than root value, find the node in the left subtree
		root.left = deleteNode(root.left, key)
	elif root.val < key: # if key value is greater than root value, find the node in right subtree
		root.right= deleteNode(root.right, key)
	else: #if we found the node (root.value == key), start to delete it
		if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
			return root.left
		if not root.left: # if it has no left children, we delete the node then new root would be root.right
			return root.right
               # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
		temp = root.right
		mini = temp.val
		while temp.left:
			temp = temp.left
			mini = temp.val
		root.val = mini # replace value
		root.right = deleteNode(root.right,root.val) # delete the minimum node in right subtree
	return root



# mine
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def helper(root, key, need_left, need_right):
            if not root:
                return None, None

            if need_left:
                if not root.right:
                    return root, root.left
                else:
                    next_val, new_right = helper(root.right, key, need_left, need_right)
                    root.right = new_right
                    return next_val, root
            if need_right:
                if not root.left:
                    return root, root.right
                else:
                    next_val, new_left = helper(root.left, key, need_left, need_right)
                    root.left = new_left
                    return next_val, root

            if root.val == key:
                replacement, new_left = helper(root.left, key, True, False)
                if replacement:
                    root.val = replacement.val
                    root.left = new_left
                else:
                    replacement, new_right = helper(root.right, key, False, True)
                    if replacement:
                        root.val = replacement.val
                        root.right = new_right
                    else:
                        return None, None # delete current

            temp1, root.left = helper(root.left, key, False, False)
            temp2, root.right = helper(root.right, key, False, False)
            return (temp1 if temp1 else temp2), root
        temp, root = helper(root, key, False, False)
        return root

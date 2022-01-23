# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# return p or q or None
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right





class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def helper(node, p, q):
            if node is None:
                return False, False
            # print(f"node={node.val}")
            lp, lq = helper(node.left, p, q)
            rp, rq = helper(node.right, p, q)
            if node.val == p.val:
                if lq or rq:
                    self.res = node
                    return False, False
                return True, False
            if node.val == q.val:
                if lp or rp:
                    self.res = node
                    return False, False
                return False, True

            # print(f"node={node.val} lp={lp} lq={lq} rp={rp} rq={rq} ")
            if (lp and rq) or (lq and rp):
                self.res = node
                return False, False
            else:
                return (lp or rp), (lq or rq)
        helper(root, p, q)
        return self.res

def createTree(a, pos):
    if pos >= len(a):
        return None
    root = TreeNode(a[pos])
    root.left = createTree(a, 2*pos+1)
    root.right = createTree(a, 2*pos+2)

if __name__ == "__main__":
    s = Solution()
    root = createTree([3,5,1,6,2,0,8,None,None,7,4], 0)
    print(s.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)))

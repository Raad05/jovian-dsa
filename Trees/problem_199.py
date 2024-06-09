# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res = []

        def preOrder(root):
            if not root:
                return
            
            res.append(root.val)
            preOrder(root.right)

        preOrder(root)

        return res
        
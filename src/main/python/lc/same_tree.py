# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (p is not None) != (q is not None):
            return False
        if (p is not None) and (q is not None):
            if p.val != q.val:
                return False
            else: 
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return True

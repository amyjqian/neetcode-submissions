# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.common = -1

        def ancestor(node, p , q):
            if node == p or node == q:
                self.common = node
                return 
            if p.val < node.val and q.val < node.val:
                return ancestor(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                return ancestor(node.right, p, q)
            else:
                self.common = node
                return 
        
        ancestor(root, p, q)
        return self.common


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_depth(root, 0)

    def get_depth(self, root, depth):
        if not root:
            return depth
        else:
            return 1 + max(self.get_depth(root.left, depth), self.get_depth(root.right, depth))





        
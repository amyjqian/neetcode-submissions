# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False
        stack = [root]
        best = 0
        while stack:
            val = stack.pop()
            best = max(best, self.get_depth(val.left) + self.get_depth(val.right))
            if val.left:
                stack.append(val.left)
            if val.right:
                stack.append(val.right)
        return best

        
    
    def get_depth(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.get_depth(node.left), self.get_depth(node.right))
            

        
        
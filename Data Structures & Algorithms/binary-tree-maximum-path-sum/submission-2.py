# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # start at leaf 
        # calculate largest path up
        # longest path at node can either be: 
            # node.val
            # node.val + node.left.val
            # node.val + node.right.val 
            # node.val + node.left.val + node.right.val 
        # hashmap to track 

        self.ans = -math.inf 

        def longest(node):
            if not node:
                return 0
            left = longest(node.left)
            right = longest(node.right) 
            left = max(left, 0)
            right = max(right, 0)

            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right) 
        
        longest(root)
        return self.ans

        
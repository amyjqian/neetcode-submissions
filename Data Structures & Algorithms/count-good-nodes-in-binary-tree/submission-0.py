# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def find_big(node, biggest):
            if not node:
                return 0
            if node.val >= biggest:
                return 1 + find_big(node.left, node.val) + find_big(node.right, node.val)
            else:
                return find_big(node.left, biggest) + find_big(node.right, biggest)
        
        ans = find_big(root, -1000)
        return ans
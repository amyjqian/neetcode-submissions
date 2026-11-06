# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pre order traversal 
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            else:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, -math.inf, math.inf)


        # if not root:
        #     return True
        
        # queue = deque([root])
        # while queue:
        #     for i in range(len(queue)):
        #         value = queue.popleft()
        #         if value.left:
        #             if value.val <= value.left.val:
        #                 return False
        #             queue.append(value.left)
        #         if value.right:
        #             if value.val >= value.right.val:
        #                 return False
        #             queue.append(value.right)
        # return True
        
        

        
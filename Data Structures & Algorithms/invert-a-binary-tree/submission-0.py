from queue import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs search 
        if not root:
            return root

        queue = deque([root])
        
        while queue:
            val = queue.popleft()
            left, right = val.left, val.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            val.left, val.right = right, left
        return root


            


    
        

        
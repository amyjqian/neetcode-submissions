# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs 
        self.ans = []
    
        def dfs(root):
            # print(root.val)
            if root.left:
                dfs(root.left)

            self.ans.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)
        # print(self.ans)
        return self.ans[k - 1]






        
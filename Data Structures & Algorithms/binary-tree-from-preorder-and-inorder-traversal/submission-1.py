# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder first element is left most 
        # preorder first elment is root 
        # left subtree = inorder first - index of preorder
        index = {v:i for i, v in enumerate(inorder)}

        def tree(i, left, right):
            if left > right:
                return 
            node = TreeNode(preorder[i])
            mid = index[node.val]
            node.left = tree(i + 1, left, mid - 1)
            node.right = tree(i + mid - left + 1, mid + 1, right)
            return node
        
        return tree(0, 0, len(preorder) - 1)


        
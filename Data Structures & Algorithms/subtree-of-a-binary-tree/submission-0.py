# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            value = stack.pop()
            if value.val == subRoot.val:
                is_subtree = self.subtree(value, subRoot)
                if is_subtree:
                    return True
            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)
        return False
        


    def subtree(self, root, subroot):
        s = [(root, subroot)]
        while s:
            val1, val2 = s.pop()
            if not val1 and not val2:
                continue
            if not val1 or not val2:
                return False
            if val1.val != val2.val:
                return False
            s.append((val1.left, val2.left))
            s.append((val1.right, val2.right))
        return True

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            val1 = stack1.pop()
            val2 = stack2.pop()
            if not (val1 and val2) or (not val1 and not val2):
                return False
            if val1.val != val2.val:
                return False
            if (val1.left and not val1.left) or (not val1.left and val2.left):
                return False
            if (val1.right and not val1.right) or (not val1.right and val2.right):
                return False
            if val1.left:
                stack1.append(val1.left)
                stack2.append(val2.left)
            if val1.right:
                stack1.append(val1.right)
                stack2.append(val2.right)
        if stack1 or stack2:
            return False
        return True
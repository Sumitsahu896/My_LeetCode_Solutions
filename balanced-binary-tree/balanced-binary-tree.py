# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedhelper(self, root):
        if not root:
            return True, -1
        
        leftIsBalanced, leftHeight = self.isBalancedhelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedhelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedhelper(root)[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # implement by inorder/preorder simutaniously
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        hashmap = {}
        ans = []
        def dfs(root):
            nonlocal ans, hashmap
            # not node
            if not root: return [None], [None]
            # if there is a node
            lin, lpre = dfs(root.left)
            c = [root.val]
            rin, rpre = dfs(root.right)

            # construct inorder / preorder
            inorder = tuple(lin + c + rin)
            preorder = tuple(c + lpre + rpre)

            # hash it in to hashmap
            if (preorder, inorder) in hashmap:
                if hashmap[(preorder, inorder)]:
                    ans.append(root)
                    hashmap[(preorder, inorder)] = 0
            else: 
                hashmap[(preorder, inorder)] = 1
            return lin + c + rin, c + lpre + rpre
            
        dfs(root)

        return ans
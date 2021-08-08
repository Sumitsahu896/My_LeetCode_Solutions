# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # For a node to be a FBT, his left child and right child should be a FBT. 
        # Also, there are no full binary trees with a positive, even number of nodes.
        
        # So, we will use the cashing that is memoization method for this.
        
        if n not in Solution.memo:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
                Solution.memo[n] = ans
                
        return Solution.memo[n]
# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        
        # RECURSIVE SOLUTION:
        # if not p and not q:
        #     return True
        # if not q or not p:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        
        # SINCE STACK(LIFO) IS USED, IT'S A DEPTH FIRST SEARCH, L TO R ORR TO L COULD BE CANGED
        # stack = [(p, q)]
        # while stack:
        #     (p, q) = stack.pop()
        #     if p and q and p.val == q.val:
        #         stack.extend([
        #             (p.right, q.right),
        #             (p.left, q.left)
        #         ])
        #     elif p or q:
        #         return False
        # return True
    
#         # SINCE QUEUE(FIFO) IS USED, IT'S A BREADTH FIRST SEARCH
#         def check(p, q):
#             if not p and not q:
#                 return True
#             if not p or not q:
#                 return False
#             if p.val != q.val:
#                 return False
#             return True
        
#         deq = deque([(p, q),])
#         while deq:
#             p, q = deq.popleft()
#             if not check(p, q):
#                 return False
            
#             if p:
#                 deq.append((p.left, q.left))
#                 deq.append((p.right, q.right))
                
#         return True
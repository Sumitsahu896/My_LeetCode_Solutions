# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity : O(nlogn), Space Complexity : O(n) where n is the total number of nodes
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        
        head = point = ListNode(0)
        for i in lists:
            while i:
                self.nodes.append(i.val)
                i = i.next
        
        for j in sorted(self.nodes):
            point.next = ListNode(j)
            point = point.next
            
        return head.next
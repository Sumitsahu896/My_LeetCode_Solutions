# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # This is a safe operation, since the input is guaranteed to be non-empty
        num = head.val
        # Till the next of the linked list is not none
        while head.next:
            # The apraoach: num = num * 2 + x ,where x is the val 
            num = num * 2 + head.next.val
            head = head.next
            
        return num
    
    
# Explanation 1
#     If we are doing any calculus by hand then we typically start from LSB to MSB.

# Here, when we traverse the linked list from head to tail(last node) then the order is MSB to LSB.

# But as we keep traversing the linked list, the previously visited nodes (imagine digit in binary representation) are kind of shifting to left by 1. Left shift by 1 = multiply by 2.

# Since each node (digit) can hold either 0 or 1 - adding the recent most visited node (or bit operation i.e. OR) is equivalent to updating the current "LSB" in the nodes traversed so far.

# Example: 7 = 111
# step1: you are looking at head i.e. so far you only have 1.

# step2: you are looking at middle digit, but in the process the previously visited digit should shift to left by 1 in its binary representation. So, you do the left shift operation with the result so far and then add the current digit. So, at the end of this step, you have 11 (in binary) i.e. 3

# step3: similar to step2, binary = 11 needs to move to the left by 1 i.e. 110. Now at the LSB, you want to slam whatever is the current digit i.e. 1. So, you end up with binary = 111 i.e. 7 in decimal.

# Hope this breakdown helps you visualize the idea and the steps.

# Explanation 2

# The first method is the same as yours but clever:
# =1
# =(1x2 + 0)
# =(1x2 + 0)x2 + 1
# =1x2x2 + 0x2 + 1
# =1x2² + 0x2 + 1
# =5
# The second is just bitwise operation:
# << means multiply by two (move to left)
# | means the or operation for bits (logic operator)

# 2x2 = 1 << 1 = 10b (move binary representation to left)
# 3 = 11b = 10 | 1 (1 or 0 is one)

# So:
# 1 = 1
# 2 = 1 << 1 | 0 = 10
# 5 = 10 << 1 | 1 = 101

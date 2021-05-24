class Solution:
#     def climbStairs(self, n: int) -> int:
#         if (n == 1):
#             return 1
#         first = 1
#         second = 2
#         for i in range(3, n+1):
#             third = first + second
#             first = second
#             second = third
        
#         return second
    def __init__(self):
            self.dict = {1:1, 2:2}
    
    
    def climbStairs(self, n: int) -> int:    
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]
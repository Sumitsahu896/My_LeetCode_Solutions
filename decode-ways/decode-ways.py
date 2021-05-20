# class Solution:
#     @lru_cache(maxsize = None)
    
#     def recursiveWithMemo(self, index: int, s: str) -> int:
#         # If you reach the end of the stirng
#         # Return 1 for success
#         if index == len(s):
#             return 1
        
#         # If the string starts with a 0, it can't be declared
#         if s[index] == '0':
#             return 0
        
#         if index == len(s) - 1:
#             return 1
        
#         answer = self.recursiveWithMemo(index + 1, s)
#         if int(s[index : index + 2]) <= 26:
#             answer += self.recursiveWithMemo(index + 2, s)

#         return answer
        
            
#     def numDecodings(self, s: str) -> int:
#         return self.recursiveWithMemo(0, s)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        
        dp[0] = 1
        
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):
            if s[i -1] != '0':
                dp[i] = dp[i - 1]
                
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
                
                
        return dp[len(s)]
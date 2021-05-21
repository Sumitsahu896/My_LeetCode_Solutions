class Solution:
    # def longestPalindrome(self, s: str) -> str:
#         # Approach 1: Longest common substring
#         if s is "":
#             return s
        
#         rev = s[::-1]
#         dp = [[0 for i in range(len(s))] for j in range(len(s))]
#         max_len = 0
#         max_end = 0
        
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if s[i] == rev[j]:
#                     if i == 0 or j == 0:
#                         dp[i][j] = 1
#                     else:
#                         dp[i][j] = dp[i - 1][j - 1] + 1
#                 if dp[i][j] > max_len:
#                     if i - dp[i][j] + 1 == len(s) - 1 - j:
#                         max_len = dp[i][j]
#                         max_end = i
                        
#         return s[max_end - max_len + 1: max_end + 1]
          
    def longestPalindrome(self, s: str) -> str:
        # Approach 2: Expand from the center
        self.maxlen = 0
        self.start = 0
        
        for i in range(len(s)):
            self.expandFromCenter(s, i, i)    # rac-e-car There might be palindromes which are odd in number
            self.expandFromCenter(s, i, i + 1) # aab-baa There might be palindromes which are even in number
    
        return s[self.start:self.start+self.maxlen]
    
    def expandFromCenter(self, s: str, left: int, right: int):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        if self.maxlen < right - left -1:
            self.maxlen = right - left - 1
            self.start = left + 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sourceLen, targetLen = len(s), len(t)
        
        if sourceLen == 0:
            return True
        
        dp = [[0] * (targetLen + 1) for _ in range(sourceLen + 1)]
        
        for col in range(1, targetLen + 1):
            for row in range(1, sourceLen + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
                    
            if dp[sourceLen][col] == sourceLen:
                return True
            
        return False
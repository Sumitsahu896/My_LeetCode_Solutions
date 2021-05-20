class Solution:
    @lru_cache(maxsize = None)
    
    def recursiveWithMemo(self, index: int, s: str) -> int:
        # If you reach the end of the stirng
        # Return 1 for success
        if index == len(s):
            return 1
        
        # If the string starts with a 0, it can't be declared
        if s[index] == '0':
            return 0
        
        if index == len(s) - 1:
            return 1
        
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer
        
            
    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)
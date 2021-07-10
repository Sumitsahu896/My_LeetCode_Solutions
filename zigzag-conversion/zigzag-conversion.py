class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        row = 0
        res = [[] for _ in range(numRows)]
        delta = -1
        
        # itereate through the string
        for char in s:
            res[row].append(char)
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
            
            
        # Consiladate the results
        for i in range(len(res)):
            res[i] = ''.join(res[i])
            
        return ''.join(res)
        
        
        
        
        
#         if numRows == 1 or numRows >= len(s):
#             return s
        
#         L = [""] * numRows
        
#         index, step = 0, 1
        
#         for x in s:
#             L[index] += x
#             if index == 0:
#                 step = 1
#             elif index == numRows - 1:
#                 step = -1
#             index += step
                
                
#         return ''.join(L)
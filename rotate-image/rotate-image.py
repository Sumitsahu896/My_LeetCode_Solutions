class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix[0])
        # for i in range(n // 2 + n % 2): # To find the mid point to which we have to run
        #     for j in range(n // 2):
        #         temp = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - i - 1][n - j - 1]
        #         matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
        #         matrix[j][n - i - 1] = matrix[i][j]
        #         matrix[i][j] = temp
        
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        return matrix
        
        
#         self.transpose(matrix)
#         self.reflect(matrix)
        
#     def transpose(self, matrix):
#             n = len(matrix)
#             for i in range(n):
#                 for j in range(i , n):
#                     matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
#     def reflect(self, matrix):
#             n = len(matrix)
#             for i in range(n):
#                 for j in range(n // 2 + n % 2):
#                     matrix[i][j], matrix[i][-j - 1] = matrix[i][-j -1], matrix[i][j]
                    
                    
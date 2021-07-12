class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        result = 0
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        result += 1
                    else:
                        cell_val = min(matrix[row - 1][col - 1], matrix[row][col - 1], matrix[row - 1][col]) + matrix[row][col]
                        result += cell_val
                        matrix[row][col] = cell_val
                        
        return result
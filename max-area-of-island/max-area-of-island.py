class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        
        def area(r, c):
            if not(0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):    
                return 0
            seen.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) + area(r, c - 1) + area(r, c + 1))
        
        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
        
        
        
# class Solution:
#     def traverseNode(self, i, j, grid, visited, sizes):
#         currentLandSize = 0
#         nodeToExplore = [[i, j]]
        
#         while len(nodeToExplore):
#             currentNode = nodeToExplore.pop()
#             i = currentNode[0]
#             j = currentNode[1]
            
#             if visited[i][j]:
#                 continue
#             visited[i][j] = True
#             if grid[i][j] == 1:
#                 continue
#             currentLandSize += 1
#             unvisitedNeighbors = self.getUnvisitedNeighbors(i, j, grid, visited)
#             for neighbor in unvisitedNeighbors:
#                 nodeToExplore.append(neighbor)
                
#         if currentLandSize > 0:
#             sizes.append(currentLandSize)
            
#     def getUnvisitedNeighbors(self, i, j, grid, visited):
#         unvisitedNeighbors = []
#         if i > 0 and not visited[i - 1][j]:
#             unvisitedNeighbors.append([i - 1, j])
#         if i < len(grid) - 1 and not visited[i + 1][j]:
#             unvisitedNeighbors.append([i + 1, j])
            
#         if j > 0 and not visited[i][j - 1]:
#             unvisitedNeighbors.append([i, j - 1])
#         if j < len(grid) - 1 and not visited[i][j + 1]:
#             unvisitedNeighbors.append([i, j + 1])
            
#         return unvisitedNeighbors        
    
            
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         sizes = []
#         visited = [[False for value in row] for row in grid]
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if visited[i][j]:
#                     continue
                    
#                 self.traverseNode(i, j, grid, visited, sizes)
#         return sizes
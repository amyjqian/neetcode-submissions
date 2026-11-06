from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # breadth first search 
        # traverse each direction for each spot 
        treasures = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i,j))
        
        queue = deque(treasures)

        while queue:
            val = queue.popleft()
            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            for d in directions:
                x1, x2 = val[0] + d[0], val[1] + d[1]
                if 0 <= x1 < len(grid) and 0 <= x2 < len(grid[0]) and grid[x1][x2] == 2147483647:
                    grid[x1][x2] = grid[val[0]][val[1]] + 1
                    queue.append((x1, x2))

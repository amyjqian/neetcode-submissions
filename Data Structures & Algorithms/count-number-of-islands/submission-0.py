from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = deque([(i, j)])
                    grid[i][j] = "-1"
                    while queue:
                        val = queue.popleft()
                        print(val)
                        x1 = val[0]
                        x2 = val[1]
                        grid[x1][x2] == "-1"
                        if x1 > 0 and grid[x1 - 1][x2] == "1":
                            queue.append((x1-1, x2))
                            grid[x1-1][x2] = "-1"
                        
                        if x1 < len(grid) - 1 and grid[x1 + 1][x2] == "1":
                            queue.append((x1+1, x2))
                            grid[x1+1][x2] = "-1"
                        
                        if x2 > 0 and grid[x1][x2-1] == "1":
                            queue.append((x1, x2-1))
                            grid[x1][x2-1] = "-1"
                        
                        if x2 < len(grid[0]) - 1 and grid[x1][x2+1] == "1":
                            queue.append((x1, x2 + 1))
                            grid[x1][x2+1] = "-1"
                    count += 1
        return count
        
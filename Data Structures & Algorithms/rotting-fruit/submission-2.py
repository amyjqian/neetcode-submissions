from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        queue = deque(rotten)
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                val = queue.popleft()
                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                for d in directions:
                    x1, x2 = val[0] + d[0], val[1] + d[1]
                    if 0 <= x1 < len(grid) and 0 <= x2 < len(grid[0]) and grid[x1][x2] == 1:
                        grid[x1][x2] = 2
                        fresh -= 1
                        if fresh == 0:
                            return count
                        queue.append((x1, x2))
        return -1



        


        
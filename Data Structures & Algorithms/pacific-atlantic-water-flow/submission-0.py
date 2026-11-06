class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs 
        # start from borders 
        # traverse if taller 
        # store hashmap of every index reachable 
        # if both pacifiic and atlantic it is true 

        # coordinates 

        borders_pacific = []
        for i in range(len(heights[0])):
            borders_pacific.append((0, i))
        for i in range(1, len(heights)):
            borders_pacific.append((i, 0))

        pac_visited = set(borders_pacific)

        stack1 = borders_pacific
        while stack1:
            val = stack1.pop()
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for d in directions:
                x1, x2 = val[0] + d[0], val[1] + d[1]
                if 0 <= x1 < len(heights) and 0 <= x2 < len(heights[0]) and (x1, x2) not in pac_visited and heights[x1][x2] >= heights[val[0]][val[1]]:
                    pac_visited.add((x1, x2))
                    stack1.append((x1,x2))
        
        border_atlantic = []
        for i in range(len(heights[0])):
            border_atlantic.append((len(heights) - 1, i))
        for i in range(0, len(heights) - 1):
            border_atlantic.append((i, len(heights[0]) - 1))

        atl_visited = set(border_atlantic)

        stack2 = border_atlantic
        while stack2:
            val = stack2.pop()
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for d in directions:
                x1, x2 = val[0] + d[0], val[1] + d[1]
                if 0 <= x1 < len(heights) and 0 <= x2 < len(heights[0]) and (x1, x2) not in atl_visited and heights[x1][x2] >= heights[val[0]][val[1]]:
                    atl_visited.add((x1, x2))
                    stack2.append((x1,x2))
        
        res = []
        for pos in pac_visited:
            if pos in atl_visited:
                res.append(pos)
        return res





        
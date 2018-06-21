class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j, grid, aera):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            area[0] += 1
            for d in direction:
                dfs(i + d[0], j + d[1], grid, area)
            return True
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = [0]
                if dfs(i, j, grid, area):
                    result = max(result, area[0])
        return result

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
# 6

grid = [[0,0,0,1,1,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
# 2

grid = [[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
# 0

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def isValid(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row: int, col: int) -> None:
            for dirX, dirY in directions:
                newY = row + dirY
                newX = col + dirX
                if isValid(newY, newX) and (newY, newX) not in seen and grid[newY][newX] == "1":
                    seen.add((newY, newX))
                    dfs(newY, newX)

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    seen.add((r, c))
                    dfs(r, c)
                    islands += 1
        
        return islands

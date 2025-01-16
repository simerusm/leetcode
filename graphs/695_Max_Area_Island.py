class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()
        max_area = 0

        def isValid(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row: int, col: int) -> int:
            area = 1
            for dirHori, dirVert in directions:
                newRow, newCol = row + dirVert, col + dirHori 
                if (newRow, newCol) not in seen and isValid(newRow, newCol) and grid[newRow][newCol] == 1:
                    seen.add((newRow, newCol))
                    area += dfs(newRow, newCol)
            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)

        return max_area

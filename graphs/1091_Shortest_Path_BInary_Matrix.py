class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1

        def isInBounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)

        seen = {(0, 0)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] # include diagonals
        q = deque([(0, 0, 1)]) # store the coordinates, (row, col, currLen)
        while q:
            currRow, currCol, currLen = q.popleft()

            if currRow == len(grid) - 1 and currCol == len(grid) - 1:
                return currLen

            for dirRow, dirCol in directions:
                if isInBounds(dirRow + currRow, dirCol + currCol) and grid[dirRow + currRow][dirCol + currCol] == 0 and  (dirRow + currRow, dirCol + currCol) not in seen:
                    seen.add((dirRow + currRow, dirCol + currCol))
                    q.append((dirRow + currRow, dirCol + currCol, currLen + 1))

        return -1

"""
- We need to do BFS in this case because if we did a DFS and went down a sub-optimal path that crosses the optimal path, a node in the optimal path would be added to the seen set thus not allowing us to go down the optimal path
- With BFS, we can guarantee that for every node we reach, we reached it via the most optimal path so putting it on the seen set, we don’t have to worry about not having the most optimal amount of distance
- Basically what we want to do is check for the base cases, if the beginning or end is a 1, then we physically can’t reach the beginning or end since we need to only traverse through 0’s
- Then we want to initialize a direction array that contains all 8 possible directions you can go
- Since it’s BFS, we want to use a queue, so use a deque to pop from the front O(1)
- As for what we’re adding to the queue, we want to add the coordinates along with the length from the beginning which is ultimately just the optimal length for that given node
- Carry out normal BFS, while the queue isn’t empty, take the left-most element on the queue, check to see if we’ve reached the end
  - If we did reach the end return the currLen we’re storing because it’s guaranteed to be the optimal length
  - Then loop through the directions array and consider all possible directions, making sure you haven’t seen something already and checking for if its in bounds and if the value is 0
  - If all that is true, then add it to the queue as another possibility to explore when it is its turn off the queue, and make sure to add 1 to the length to reach that node
- Time complexity: O(n^2) because we could end up looping through the entire NxN 2D array 
- Space complexity: O(N^2) because we can end up adding every single node on to the seen set as well

"""

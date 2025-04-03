from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]

        q = deque()
        seen = set()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    q.append((row, col, 1))
                    seen.add((row, col))

        def isValid(r, c) -> bool:
            return 0 <= r < len(mat) and 0 <= c < len(mat[0]) and (r, c) not in seen
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            currRow, currCol, currDist = q.popleft()
            for dirRow, dirCol in directions:
                if isValid(currRow + dirRow, currCol + dirCol) and mat[currRow + dirRow][currCol + dirCol] == 1:
                    res[currRow + dirRow][currCol + dirCol] = currDist
                    q.append((currRow + dirRow, currCol + dirCol, currDist + 1))
                    seen.add((currRow + dirRow, currCol + dirCol))
        
        return res

"""
- Use BFS to solve this
- There is a very slow solution that does work, but if inefficient, where we loop through all elements in the matrix and do a BFS on every single 1 and count the number of steps it takes to reach a 0
  - This is like O(n^2 x m^2) and very slow
  - Each 1 would have its own visited and BFS state, there's no global state
- The faster way is to do a BFS starting for all 0s and keeping a global state of a seen set
- Since BFS guarantees that you’ll reach every node in the least amount of steps if you start from a 0, then keep track of the number of steps it takes to get to a specific point in the matrix
- For that row and col, if it’s a 1 in the mat matrix then update the new result array at that index as to how many steps it took to get there
- On the queue, we have a tuple of this structure
  - (row, col, least # of steps to get here)
  - Doing this, we can keep a global seen state as we do BFS starting from every 0
- Initiallly, pre-process the matrix and append all the 0’s (row, col, 1) onto the queue and then BFS with that queue
- Time complexity: O(r*c) where r is the number of rows and c is the number of columns, the BFS itself is O(r*c) since we visit each node at least once and the pre-process step is O(r*c) so it’d be O(2*r*c) which gets amortized to O(r*c) or just O(n) where n is the number of elements (n = r*c)
- Space complexity: O(n) or O(r*c), depending on how you view it, since we’re going to be putting all elements on the seen set
"""

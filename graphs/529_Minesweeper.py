class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        clickY, clickX = click[0], click[1]
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]

        def isValid(r: int, c: int) -> bool:
            '''
            Check if the board square to check is in bounds of the board dimensions
            '''
            return 0 <= r < len(board) and 0 <= c < len(board[0]) 

        def checkBomb(r: int, c: int) -> int:
            '''
            Returns the number of bombs that neighbour the current square
            '''
            bombCount = 0
            for dY, dX in directions:
                nY = dY + r
                nX = dX + c
                if isValid(nY, nX) and board[nY][nX] == "M":
                    bombCount += 1
            return bombCount

        def dfs(r: int, c: int) -> None:
            '''
            Traverses the board via dfs,
                - check if we're near a bomb
                - if near a bomb, turns the E into a number from 1-8
                - else, turn the square to B
                - add neigbhours to dfs stack
            '''
            bombCount = checkBomb(r, c)
            if bombCount > 0:
                board[r][c] = str(bombCount)
            else:
                board[r][c] = 'B'
                for dirY, dirX in directions:
                    newY = dirY + r
                    newX = dirX + c
                    
                    if isValid(newY, newX) and board[newY][newX] == 'E':
                        print(newY, newX)
                        dfs(newY, newX)
            

        if board[clickY][clickX] == "M":
            board[clickY][clickX] = "X"
        else:
            dfs(clickY, clickX)

        return board

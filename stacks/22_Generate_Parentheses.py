class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possibilities = []
        
        def backtrack(leftPar: int, rightPar: int, curr: List[str] = []) -> None:
            if leftPar == n and rightPar == n:
                possibilities.append("".join(curr))
                return
            
            if leftPar < n:
                curr.append("(")
                backtrack(leftPar + 1, rightPar, curr)
                curr.pop()
            if rightPar < leftPar:
                curr.append(")")
                backtrack(leftPar, rightPar + 1, curr)
                curr.pop()
        
        backtrack(0, 0)
        return possibilities

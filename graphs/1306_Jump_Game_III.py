class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque
        q = deque([start]) # ind, curr steps to get to ind
        seen = {start}

        def isValid(index: int) -> bool:
            return 0 <= index < len(arr) and index not in seen

        while q:
            currInd = q.popleft()
            if arr[currInd] == 0:
                return True
            options = [arr[currInd], -arr[currInd]]
            for nextStep in options:
                if isValid(currInd + nextStep):
                    q.append(currInd + nextStep)
                    seen.add(currInd + nextStep)

        return False

"""
- This is an implicit BFS graph problem
- Whenever we do BFS, we’re just checking to see if we’re able to reach an index that has a value of 0 in the array
- The queue and seen data structures only need to store the index we’ve been on, this is because we don’t need to count the number of steps to get to a particular index as distinct since if the only way to get to a index with value 0 is through a certain node, no matter how many paths there are to get to that certain node, you just need to get to it since we’re returning true or false in the end eventually and not finding the # of different ways to get there
- In the BFS logic, subtract or add the current value of the array at a particular index and check if its within the bound of the array length and not in seen
- Return false at the end if everything has been exhausted
- Time complexity: O(n) where n is the length of the array, at most we’ll go over every single index
- Space complexity: O(n) where n is the length of the array, at most we’ll store every index
"""

import heapq
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats

"""
- Greedy solution with sorting
- Sort the array and then create two pointers
- Decrement the right pointer in every iteration, we want to optimize exhausting the larger numbers first and then wherever possible pair it with a samller number if its possible
  - If a pair is possible, then increment the left pointer too
  - Stop once left becomes bigger than right
- Time Complexity: O(nlogn) + O(n) --> O(nlogn), O(nlogn) due to Timesort time complexity and O(n) due to iterating through the sorted array once, ammortized to O(nlogn)
- Space Complexity: O(1) - it theoretically should be O(n) since Timesort is just a spin off of merge sort and utilizes O(n) space worst case, however Leetcode doesn't count that as space used by the user thus it's considered O(1)
"""

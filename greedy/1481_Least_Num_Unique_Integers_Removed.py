from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = [(freq, elem) for elem,freq in Counter(arr).items()]
        heapq.heapify(heap)

        while k > 0:
            freq, _ = heapq.heappop(heap)
            if k - freq < 0:
                return len(heap) + 1
            k -= freq
        return len(heap)

"""
- greedy algo problem
- create a frequency hash map using counter and then reverse the key value pairs and turn it into a list of tuples, turn this into a min heap
- while the amount of elements we can remove (k) is positive, pop the min element from the heap and test to see if we can remove all those specific elements via the frequency of the element
    - if we can't, return the length of the heap + 1 to account for the element we just popped since we can't remove all its elements fully thus contributing to the distinct elements that will be present
    - if we can, subtract the frequency of the element we're removing from the total number of elements we can remove (k)
- Time Complexity: O(nlogn) due to the heap creation operation
- Space Complexity: O(n) since worst case every element in the array is unique so we'd be creating a heap that contains every element in the array and its frequency of 1
"""

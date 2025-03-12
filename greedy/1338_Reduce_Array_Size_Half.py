from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        freq_arr = Counter(arr)
        sorted_freq_arr = sorted(freq_arr.items(), key=lambda key_val: key_val[1], reverse=True)

        curr_size = size # this makes a copy of size, its not a reference to size
        idx = 0
        deletions = 0
        while curr_size > size/2 and idx < size:
            curr_size -= sorted_freq_arr[idx][1]
            deletions += 1
            idx += 1
        return deletions

"""
- Greedy algo problem with sorting
- We don't need to worry about actually removing the values from the original array, we can just work with the frequency of elements with in it
- Get freq by using Counter and then sort this freq dict using a lambda function and sort by the values of the key value pairs bundled in a tuple after doing .items()
  - Make sure to reverse it since we want it in decreasing order and greedily get rid of the highest occuring elements
- Run a while loop that iterates over the sorted array of tuples and removes the highest occuring values from a temp current sum variable and keep checking to see if we're below half of the original size
- Time Complexity: O(nlogn) due to sorting
- Space Complexity: O(n) since we're creating a new sorted array and not modifying it in place
"""

from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_frequencies = Counter(arr)
        arr_set = set(arr)
        elements = 0

        for num in arr_set:
            if num + 1 in arr_set:
                elements += num_frequencies[num]

        return elements

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0 for _ in range(len(spells))]
        potions.sort()

        def bin_search(spell: int) -> int:
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if potions[m] * spell >= success:
                    r = m - 1
                else:
                    l = m + 1
            return len(potions) - l

        for idx, spell in enumerate(spells):
            num = bin_search(spell)
            res[idx] = num
        return res

"""
- Binary search optimization problem
- Sort the potions and then for spell, binary search to find the index at which every element starting from that index the potion magnitudes satsify the constraint
- Binary search
  - Set up standard binary search with condition l <= r
  - If we meet/exceed our success criteria, move the right pointer to the left everytime, we're trying to find the smallest index, else move the left one up one
  - When we break the condition, return the length of the potions - left pointer index after the search, this will get the # of elements from the pointer to the end of the array
- Time Complexity: O(nlogn) + O(mlogn) = O((n+m)logn), nlogn because we sort potions at the start, mlogn for binary search * iteration through spells where m is number of elements in spells and n is number of elements in potions
- Space Complexity: O(1) by leetcode standards, however timsort is O(nlogn) space complexity under the hood
"""

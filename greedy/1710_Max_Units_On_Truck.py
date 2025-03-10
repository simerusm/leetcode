class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        max_units = 0
        total_boxes = 0

        for i in range(len(boxTypes)):
            num_boxes, units_per_box = boxTypes[i]
            
            if total_boxes + num_boxes <= truckSize:
                total_boxes += num_boxes
                max_units += units_per_box * num_boxes
            else:
                difference = truckSize - total_boxes
                total_boxes += difference
                max_units += difference * units_per_box
                return max_units
        return max_units

"""
- Greedy solution via sorting
- Sort by the number of units per box in reverse order because we want to optimize for number of units per box
- Iterate through the array and if we can add all boxes to the truck make the proper additions, if not, add only what we can and then return the max units since we aren't able to add any more boxes
- Time Complexity: O(nlogn)
- Space Complexity: O(1) by Leetcode standards but O(n) in reality due to Timsort inner workings
"""

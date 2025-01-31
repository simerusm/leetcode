class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        maxHeightLeft = [0]
        maxHeightRight = [0]

        temp = height[0]
        for i in range(1, len(height)):
            temp = max(temp, height[i])
            maxHeightLeft.append(temp)

        temp = height[-1]
        for i in range(len(height) - 2, -1, -1):
            temp = max(temp, height[i])
            maxHeightRight.append(temp)
        maxHeightRight.reverse() # or [::-1]

        res = 0
        for idx in range(len(height)):
            minVal = min(maxHeightLeft[idx], maxHeightRight[idx])
            if minVal == 0:
                continue
            res += min(maxHeightLeft[idx], maxHeightRight[idx]) - height[idx]
        return res

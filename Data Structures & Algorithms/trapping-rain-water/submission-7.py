class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) space solution
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        mins = []

        currMax = 0
        for i in range(1, len(height)):
            currMax = max(currMax, height[i - 1])
            maxLeft[i] = currMax

        currMax = 0
        for i in range(len(height) - 2, -1, -1):
            currMax = max(currMax, height[i + 1])
            maxRight[i] = currMax

        for i in range(len(height)):
            mins.append(min(maxLeft[i], maxRight[i]))

        totalWater = 0
        for i in range(len(height)):
            water = mins[i] - height[i]
            if water > 0:
                totalWater += water

        return totalWater

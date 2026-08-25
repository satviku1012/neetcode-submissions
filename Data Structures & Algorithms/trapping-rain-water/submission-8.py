class Solution:
    def trap(self, height: List[int]) -> int:
        # O(1) space solution (two pointer)
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        totalWater = 0

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                totalWater += max(maxLeft - height[left], 0)
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                totalWater += max(maxRight - height[right], 0)
                maxRight = max(maxRight, height[right])

        return totalWater

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force: nested loop checking each pair of heights for the max area
        # 2 pointer: keep track of max but move pointer inward if its height is less than the other pointer's height

        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            currMax = (right - left) * (min(heights[right], heights[left]))
            if currMax > maxArea:
                maxArea = currMax

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left += 1


        return maxArea
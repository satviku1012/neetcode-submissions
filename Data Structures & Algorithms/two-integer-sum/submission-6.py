class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # val -> index

        for i in range(len(nums)):
            if target - nums[i] in map and map[target - nums[i]] != i:
                return [map[target - nums[i]], i]
            
            map[nums[i]] = i
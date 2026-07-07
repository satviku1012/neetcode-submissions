class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map and map[diff] != i:
                return [map[diff], i]
            
            map[n] = i
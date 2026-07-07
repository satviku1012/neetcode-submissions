class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}

        for x in nums:
            duplicate_map[x] = duplicate_map.get(x, 0) + 1

            if 2 in duplicate_map.values():
                return True

        return False

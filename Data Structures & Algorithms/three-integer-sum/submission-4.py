class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = []
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r: # two sum II approach
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # move both pointers inward since for each num, there is only 1 other num that can add up to the target
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result
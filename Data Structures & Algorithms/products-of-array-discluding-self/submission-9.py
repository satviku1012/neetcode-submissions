class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        pre = 1
        for i in range(len(nums)):
            # calculate prefixes and populate result with them
            result[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            # calculate postfixes and multiply with prefixes
            result[i] *= post
            post *= nums[i]

        return result
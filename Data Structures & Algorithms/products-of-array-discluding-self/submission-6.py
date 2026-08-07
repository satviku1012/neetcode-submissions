class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], []

        # get prefix array
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            nums[i] = prod
        
        # get postfix array
        prod = 1
        for i in range (len(nums) - 1, -1, -1):
            prod *= nums[i]
            nums[i] = prod

        # create result array
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(prefix[i - 1] * postfix[i + 1])
                

        
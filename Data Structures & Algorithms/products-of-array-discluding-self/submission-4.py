class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep track of indices where num == 0
        zeroInd = set()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroInd.add(i)

        # if nums is not all zeros, calculate total product excluding any zeros in nums
        if len(zeroInd) != len(nums):
            totalProd = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    totalProd *= nums[i]
        else:
            totalProd = 0

        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(zeroInd) > 1 and i not in zeroInd:
                    output.append(0)
                else:
                    output.append(totalProd)
            else:
                if len(zeroInd) != 0 and i not in zeroInd:
                    output.append(0)
                else:
                    output.append(int(totalProd/nums[i]))

        return output

        
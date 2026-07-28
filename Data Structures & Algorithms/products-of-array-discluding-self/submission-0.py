class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        
        # keep track of indices where num == 0
        zeroInd = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroInd.add(i)
            else:
                totalProd = prod * nums[i]

        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(prod)
            else:
                if len(s) != 0 and i not in zeroInd:
                    output.append(0)
                else:
                    output.append(int(prod/nums[i]))

        return output

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        
        # keep track of indices where num == 0
        zeroInd = set()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroInd.add(i)
            else:
                totalProd = totalProd * nums[i]

        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(totalProd)
            else:
                if len(zeroInd) != 0 and i not in zeroInd:
                    output.append(0)
                else:
                    output.append(int(totalProd/nums[i]))

        return output

        
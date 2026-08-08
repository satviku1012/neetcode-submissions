class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)

        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                count = 1
                prev = n
                while prev + 1 in numSet:
                    count += 1
                    prev += 1
                if count > longest:
                    longest = count

        return longest

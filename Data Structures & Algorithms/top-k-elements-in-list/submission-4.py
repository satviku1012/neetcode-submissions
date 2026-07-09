from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create freq dict for nums
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        # return k largest values in the freq dict
        top = set()

        # go thru freq dict k times to find top k maxes
        for i in range(k):
            m = -10000
            # find the next max freq that isnt in top set
            for num in freq:
                if freq[num] >= m and num not in top:
                    m = freq[num]
                    x = num
            top.add(x)

        result = []
        for num in top:
            result.append(num)

        return result
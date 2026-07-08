from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        
        # create dict of char frequency arrays as keys, and arrays of the anagrams as values
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            table[tuple(freq)].append(s)

        result = []
        for freq in table:
            result.append(table[freq])

        return result





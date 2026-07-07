from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        result = []

        for s in strs:
            group = sorted(s)
            group = tuple(group)
            table[group].append(s)

        for group in table:
            result.append(table[group])

        return result

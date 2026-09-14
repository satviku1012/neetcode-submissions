from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force
        res = 0
        
        for i in range(len(s)):
            freq = defaultdict(int)

            for j in range(i, len(s)):
                freq[s[j]] += 1
                mostFreq = max(freq.values())
                if len(s[i:j + 1]) - mostFreq <= k:
                    res = max(res, len(s[i:j + 1]))

        return res


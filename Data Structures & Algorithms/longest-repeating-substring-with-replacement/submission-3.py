from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        mostFreq = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            mostFreq = max(freq.values())

            # check if window is valid
            if right - left + 1 - mostFreq <= k:
                res = right - left + 1
            else:
                freq[s[left]] -= 1
                left += 1

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for right in range(len(s)):
            # worst case is when you have a long substring so far, but lose that streak of unique chars twice in a row at the end (need to restart the substring from length 1)
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)

        return res
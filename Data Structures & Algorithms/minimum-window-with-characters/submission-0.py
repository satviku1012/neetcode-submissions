from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            countT[c] += 1

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # pop from left side of window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        if resLen != float("infinity"):
            return s[res[0]:res[1] + 1]
        else:
            return ""

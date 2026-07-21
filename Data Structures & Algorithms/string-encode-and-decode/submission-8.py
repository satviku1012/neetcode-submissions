class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "0!02hawfah"
        
        s = ""

        for string in strs:
            s += chr(len(string)) + string

        return s

    def decode(self, s: str) -> List[str]:
        result = []

        if s == "0!02hawfah":
            return []

        while len(s) != 0:
            result.append("")
            for i in range(1, ord(s[0]) + 1):
                result[len(result) - 1] += s[i]
            s = s[ord(s[0]) + 1:]
        
        return result

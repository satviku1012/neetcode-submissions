class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""

        if strs == []:
            return "00"

        result = ""
        for i in range(len(strs) - 1):
            result += strs[i] + "😭"
        result += strs[len(strs) - 1]

        return result

    def decode(self, s: str) -> List[str]:
        if s == "00":
            return []
        
        result = s.split("😭")
        return result
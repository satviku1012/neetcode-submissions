class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and self.isAlphaNum(s[i]) == False:
                i += 1
            while j > i and self.isAlphaNum(s[j]) == False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

    def isAlphaNum(self, c: int) -> bool:
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
            return True
        return False
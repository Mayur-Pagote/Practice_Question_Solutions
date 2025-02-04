class Solution:
    def findValidPair(self, s: str) -> str:
        length = len(s)
        for i in range(1, length):
            if s[i - 1] != s[i] and s.count(s[i - 1]) == int(s[i - 1]) and s.count(s[i]) == int(s[i]):
                return s[i - 1] + s[i]
        return ""  

class Solution(object):
    def removeOccurrences(self, s, part):
        l = len(part)
        while True:
            if part in s:
                i = s.index(part)
                s = s[0:i] + s[i+l:]
            else:
                break
        return s

        

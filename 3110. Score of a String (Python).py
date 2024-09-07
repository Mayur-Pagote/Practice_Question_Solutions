class Solution(object):
    def scoreOfString(self, s):
        length = len(s) # Storing length of string s
        result = 0 # Initializing result with 0

        # Looping till length - 1 and finding difference between ASCII value of every character
        for i in range (length-1):
            result += abs(ord(s[i]) - ord(s[i+1]))
        return result

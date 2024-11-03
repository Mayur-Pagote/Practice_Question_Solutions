class Solution(object):
    def rotateString(self, s, goal):
        # Check if the lengths are equal
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself
        concatenated = s + s
        
        # Check if goal is a substring of the concatenated string
        return goal in concatenated

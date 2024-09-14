class Solution(object):
    def addDigits(self, num):
        # Return the digital root of num using the formula 1 + (num - 1) % 9
        if (num == 0):
            return 0
        else:
            return 1 + (num-1)%9
        

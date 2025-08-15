class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        num = 1
        
        while num <= n:
            if num == n:
                return True
            num *= 4
        return False

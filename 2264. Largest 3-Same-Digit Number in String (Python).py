class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = []
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                l.append(num[i:i+3])
        
        if not l:
            return ""
        
        return max(l)

class Solution(object):
    def maxFrequencyElements(self, nums):
        s = set(nums)
        f = 0
        c = 0
        for i in s:
            t = nums.count(i)
            if f == t:
                c += 1
            elif f < t:
                f = t
                c = 1
        return c*f
        

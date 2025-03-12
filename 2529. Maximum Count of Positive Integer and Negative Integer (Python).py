class Solution(object):
    def maximumCount(self, nums):
        max_neg = 0
        max_pos = 0
        for i in nums:
            if i == 0:
                continue
            elif i > 0:
                max_pos += 1
            else:
                max_neg += 1
        
        return max(max_neg, max_pos)

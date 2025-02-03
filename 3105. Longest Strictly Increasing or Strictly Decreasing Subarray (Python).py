class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        
        i_count = 1
        d_count = 1
        max_len = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                i_count += 1
            else:
                max_len = max(max_len, i_count)
                i_count = 1
            
            if nums[i] < nums[i-1]:
                d_count += 1
            else:
                max_len = max(max_len, d_count)
                d_count = 1

        return max(max_len, i_count, d_count)

        

class Solution(object):
    def longestSubarray(self, nums):
        # Find the largest number in the list
        target = max(nums)
        
        # Initialize variables for the length of the current subarray and the maximum length found
        size, res = 0, 0
        
        # Go through each number in the list
        for n in nums:
            if n == target:
                size += 1
            else:
                size = 0
            
            # Update the maximum length if needed
            res = max(res, size)
        
        return res

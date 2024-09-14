class Solution(object):
    def longestSubarray(self, nums):
        # Find the largest number in the list
        target = max(nums)
        
        # Initialize variables for the length of the current subarray and the maximum length found
        count = 0
        result = 0
        
        # Go through each number in the list
        for i in nums:
            if i == target:
                count += 1
            else:
                count = 0
            
            # Update the maximum length if needed
            result = max(result, count)
        
        return result

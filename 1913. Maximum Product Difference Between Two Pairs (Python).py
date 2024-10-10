class Solution(object):
    def maxProductDifference(self, nums):
        # Sort the list of numbers in ascending order
        nums.sort()
        
        # Calculate the product of the two largest numbers
        max_product = nums[-1] * nums[-2]
        
        # Calculate the product of the two smallest numbers
        min_product = nums[0] * nums[1]
        
        return max_product - min_product

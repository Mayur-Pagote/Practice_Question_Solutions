class Solution(object):
    def moveZeroes(self, nums):
        # Count the number of zeros in the list
        count = nums.count(0)
        
        # Loop for the number of zeros counted
        for i in range(count):
            # Remove the first occurrence of 0 from the list
            nums.remove(0)
            # Append 0 to the end of the list
            nums.append(0)

        return nums

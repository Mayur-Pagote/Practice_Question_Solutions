class Solution(object):
    def majorityElement(self, nums):
        # Create a set from the input list to get unique elements
        temp_set = set(nums)
        count = 0  # Variable to keep track of the maximum count of any element
        value = None  # Variable to store the majority element

        # Iterate through each unique element in the set
        for i in temp_set:
            # Count how many times the element appears in the original list
            if nums.count(i) > count:
                # Update count and the value if the current element has a higher count
                count = nums.count(i)
                value = i
              
        return value

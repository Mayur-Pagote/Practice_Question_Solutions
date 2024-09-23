class Solution(object):
    def singleNumber(self, nums):
        # Create a set from the list to get unique elements
        sett = set(nums)
        
        # Iterate through each unique element in the set
        for i in sett:
            # Check if the count of the current element in the original list is 1
            if nums.count(i) == 1:
                # If it appears once, return that element
                return i
            else:
                # Remove the element from the original list (not necessary for the solution)
                nums.remove(i)

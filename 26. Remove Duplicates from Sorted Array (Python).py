class Solution(object):
    def removeDuplicates(self, nums):
        # Convert the list to a set to get unique elements
        nums_set = set(nums)

        # Iterate over each unique element in the set
        for i in nums_set:
            # Initialize a temporary count for occurrences of the current element
            temp_count = 0
            # Check if the current element appears more than once in the list
            if nums.count(i) > 1:
                # If it does, store the number of times it appears
                temp_count = nums.count(i)
                # Remove all but one occurrence of the current element from the list
                for j in range(temp_count - 1):
                    nums.remove(i)

        return len(nums)

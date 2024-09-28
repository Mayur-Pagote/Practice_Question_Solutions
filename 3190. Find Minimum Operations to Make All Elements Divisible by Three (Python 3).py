class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0  # Initialize a counter to keep track of operations needed
        
        # Iterate through each number in the list
        for i in nums:
            # Check if the number can be transformed to a multiple of 3
            # This is true if either (i + 1) is a multiple of 3 or (i - 1) is a multiple of 3
            if ((i + 1) % 3 == 0) or ((i - 1) % 3 == 0):
                count += 1  # Increment the count if the condition is met
           
        return count  # Return the total count of operations needed

class Solution(object):
    def sumOfMultiples(self, n):
        # Initialize a variable to hold the sum of multiples
        num_sum = 0
        
        # Iterate through all numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Check if the current number is a multiple of 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                # If it is, add it to the running total
                num_sum += i

        return num_sum

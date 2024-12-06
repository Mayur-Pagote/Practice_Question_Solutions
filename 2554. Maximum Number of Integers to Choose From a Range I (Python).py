class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned_set = set(banned)  # Convert banned list to a set for faster lookup
        count = 0
        num_sum = 0
        
        # Iterate over all integers from 1 to n
        for i in range(1, n + 1):
            if i not in banned_set:  # Check if the number is not banned
                if num_sum + i > maxSum:  # Check if adding this number exceeds maxSum
                    break  # If it does, stop the loop
                num_sum += i  # Add the number to the sum
                count += 1  # Increment the count
        
        return count

class Solution(object):
    def shuffle(self, nums, n):
        # Split the input list 'nums' into two halves: 'x' and 'y'
        x = nums[0:n]  # First half of the array (first n elements)
        y = nums[n:]   # Second half of the array (last n elements)

        l = []  # Initialize an empty list to store the shuffled result

        # Loop through the range of n to interleave the elements from x and y
        for i in range(n):
            l.append(x[i])  # Append the i-th element from the first half
            l.append(y[i])  # Append the i-th element from the second half
        
        return l  

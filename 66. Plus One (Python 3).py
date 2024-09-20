class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []  
        rem = 0  

        num = 0  # This will hold the integer representation of the digits
        for i in digits:
            # Convert the list of digits to a single integer
            num = num * 10 + i
        num = num + 1  # Add one to the integer

        # Break down the new number into its individual digits
        while (num != 0):
            rem = num % 10  # Get the last digit (remainder)
            l.insert(0, rem)  # Insert it at the beginning of the list
            num = num // 10  # Remove the last digit from num
        return l  
        

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        # Store the original number in a temporary variable
        temp = x
        # Initialize remainder variable to store the sum of the digits
        rem = 0
        
        # Loop to calculate the sum of digits of the number
        while temp > 0:
            # Add the last digit of temp to rem
            rem = rem + temp % 10
            # Remove the last digit from temp
            temp = temp // 10
            
        # Check if the original number is a Harshad number
        # A Harshad number is divisible by the sum of its digits
        if x % rem == 0:
            # If it is a Harshad number, return the sum of the digits
            return rem
        else:
            # If it is not a Harshad number, return -1
            return -1

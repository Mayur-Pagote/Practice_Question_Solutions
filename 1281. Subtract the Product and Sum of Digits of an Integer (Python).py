class Solution(object):
    def subtractProductAndSum(self, n):
        rem = 0          
        sum_n = 0      
        product_n = 1   

        # Loop until all digits of n are processed
        while(n > 0):
            rem = n % 10  # Get the last digit of n
            sum_n += rem  # Add the digit to the sum
            product_n *= rem  # Multiply the digit to the product
            n //= 10      # Remove the last digit from n
          
        return product_n - sum_n

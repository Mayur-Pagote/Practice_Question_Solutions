class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer n to its binary representation as a string
        str_bin = str(bin(n))
        
        # Count the number of '1's in the binary string representation
        return str_bin.count("1")

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create a set of jewels for O(1) look-up time
        jewel_set = set(jewels)
        count = 0
        
        # Iterate through each stone
        for stone in stones:
            # Check if the stone is a jewel
            if stone in jewel_set:
                count += 1
        
        return count

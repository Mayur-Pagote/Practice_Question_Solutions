class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
      
        # Iterate over each word in the words list
        for i in words:
            # Initialize a temporary counter to check if all characters in the word are allowed
            temp_count = 0
            # Iterate over each character in the current word
            for j in i:
                # Check if the character is in the allowed set
                if j in allowed:
                    # Increment the temporary counter if the character is allowed
                    temp_count += 1
            
            # If the temporary counter equals the length of the word, it means all characters in the word are allowed
            if temp_count == len(i):
                count += 1

        return count

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into a list of words
        word_list = sentence.split()
        
        # Get the length of the word list minus one (to avoid index out of range)
        length = len(word_list) - 1
        
        # Loop through each word in the list except the last one
        for i in range(length):
            first = word_list[i]     # Current word
            second = word_list[i+1]  # Next word
            
            # Check if the last character of the current word
            # matches the first character of the next word
            if first[-1] != second[0]:
                return False  # Return False if they don't match
        
        # After the loop, check the first and last words
        first = word_list[0]       # First word
        second = word_list[-1]     # Last word
        
        # Check if the first character of the first word
        # matches the last character of the last word
        if first[0] != second[-1]:
            return False  # Return False if they don't match
        
        return True  # Return True if all conditions are satisfied

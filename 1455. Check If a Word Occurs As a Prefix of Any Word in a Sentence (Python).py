class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        word_list = sentence.split()  # Split the sentence into words
        count = 0  # Initialize word position counter
        for word in word_list:  # Loop through the words in the sentence
            count += 1  # Increment word position
            if word.startswith(searchWord):  # Check if the word starts with searchWord
                return count  # Return the 1-indexed position
        return -1  # Return -1 if no word starts with searchWord

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        # Initialize an empty list to store uncommon words
        temp_list = []
        
        # Convert both sentences into lists of words
        s1 = list(s1.split(" "))
        s2 = list(s2.split(" "))
        
        # Iterate through each word in the first sentence
        for i in s1:
            # Check if the word appears only once in s1 and is not in s2
            if s1.count(i) == 1 and i not in s2:
                temp_list.append(i)
                
            # Check if the word appears only once in s2 and is not in s1
            elif s2.count(i) == 1 and i not in s1:
                temp_list.append(i)
        
        # Iterate through each word in the second sentence
        for i in s2:
            # Check if the word appears only once in s1 and is not in s2
            if s1.count(i) == 1 and i not in s2:
                temp_list.append(i)
                
            # Check if the word appears only once in s2 and is not in s1
            elif s2.count(i) == 1 and i not in s1:
                temp_list.append(i)

        return temp_list

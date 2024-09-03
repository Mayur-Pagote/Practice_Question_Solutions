# This function will help in adding digits in given literal
def transformation(str_num):
        temp = 0
        for i in str(str_num):
            temp += int(i)
        return temp

class Solution(object):
    def getLucky(self, s, k):

        num_al = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }

        temp_num = "" # Variable to hold values of alphabets

        # Loop to convert alphabets into numbers
        for i in s:
            temp_num += str(num_al[i])

        # Loop to call transormation function k times
        for j in range(k):
            temp_num = transformation(int(temp_num))
        
        return temp_num

        

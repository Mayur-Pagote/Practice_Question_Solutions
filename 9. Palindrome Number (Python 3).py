class Solution:
    def isPalindrome(self, x: int) -> bool:
                
        if x == 0: # This will handle specific test case of 0
            return True
          
        elif (x < 0) or (x % 10 == 0): # This will check given number is negative or mod of 10
            return False
          
        else: 
            reverse = 0
            temp = x
            while(x>0): # This will help in reversing the given number
                rem = x%10
                reverse = reverse*10 + rem
                x = x//10
        
        return temp == reverse
        

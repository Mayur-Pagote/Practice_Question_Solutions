class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false; // THis will check number is negative or not
        
        long reverse = 0;
        long temp = x;
  
        while(x>0){ // This loop will help in reversing the number
            long rem = x%10;
            reverse = reverse*10 + rem;
            x = x/10;
        }
        return temp == reverse;
    }
};

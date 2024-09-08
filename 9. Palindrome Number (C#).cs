public class Solution {
    public bool IsPalindrome(int x) {
        if (x<0) return false; // This will check given number is negative or not
        
        long num = 0;
        long temp = x;
        
        while(x>0){ // This will reverse the given number
            long rem = x%10;
            num = num*10 + rem;
            x = x/10;
        }
        return temp == num;
        
    }
}

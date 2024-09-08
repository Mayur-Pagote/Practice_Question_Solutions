public class Solution {
    public bool IsPalindrome(int x) {
        if (x<0) return false;
        
        long num = 0;
        long temp = x;
        while(x>0){
            long rem = x%10;
            num = num*10 + rem;
            x = x/10;
        }
        return temp == num;
        
    }
}

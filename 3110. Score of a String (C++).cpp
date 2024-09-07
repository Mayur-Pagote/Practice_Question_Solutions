#include <cmath>
class Solution {
public:
    int scoreOfString(string s) {
        int length = s.size(); // Storing length of string s in length variable
        int result = 0; // Initializing result with 0

        // Looping over s and calculating difference
        for (int i = 0; i<length-1; i++){
            result += abs(s[i] - s[i+1]); 
        }
        return result;
    }
};

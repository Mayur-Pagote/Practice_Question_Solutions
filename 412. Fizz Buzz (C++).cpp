class Solution {
public:
    vector<string> fizzBuzz(int n) {
        // Initialize an empty vector to hold the results
        vector<string> fblist;
        
        // Loop from 1 to n
        for (int i = 1; i <= n; i++) {
            // Check if the number is divisible by both 3 and 5
            if (i % 3 == 0 && i % 5 == 0) {
                fblist.push_back("FizzBuzz"); // Add "FizzBuzz" for multiples of both
            }
            // Check if the number is divisible by 3 only
            else if (i % 3 == 0) {
                fblist.push_back("Fizz"); // Add "Fizz" for multiples of 3
            }
            // Check if the number is divisible by 5 only
            else if (i % 5 == 0) {
                fblist.push_back("Buzz"); // Add "Buzz" for multiples of 5
            }
            // If not divisible by either, convert the number to a string and add it
            else {
                fblist.push_back(to_string(i)); // Add the number itself
            }
        }
        return fblist;
    }
};

public class Solution {
    public int FinalValueAfterOperations(string[] operations) {

        int length = operations.Length; // This variable will store length of operations array

        int x = 0; // Initializing x with 0

        // Loop to compare operations
        for (int i = 0; i < length; i++){
            if (operations[i] == "--X") x -= 1;
            else if (operations[i] == "X--") x -= 1;
            else if (operations[i] == "++X") x += 1;
            else if (operations[i] == "X++") x += 1;
        };
    return x;
        
    }
}

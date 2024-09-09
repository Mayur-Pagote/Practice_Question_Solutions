class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
        int max = 0; // Initialize a variable to keep track of the maximum wealth
      
        int row_size = accounts.size();  // Get the number of customers
        
        int col_size = accounts[0].size(); // Get the number of accounts each customer has

        // Iterate through each customer
        for (int i = 0; i < row_size; i++) {
           
            int count = 0;
            for (int j = 0; j < col_size; j++) {
                count += accounts[i][j];
            }
            if (count > max) max = count;
        }
        return max;
    }
};

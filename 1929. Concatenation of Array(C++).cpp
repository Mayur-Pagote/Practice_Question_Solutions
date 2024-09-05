class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int len = nums.size(); // len will contain size of nums

        vector<int> temp (2*len); // Creating a temp vector with twice the length of nums

        // First loop to append elements of nums into temp
        for (int i=0; i<len; i++){
            temp[i]  = nums[i];
        }

        // Second loop to append element of nums into temp once again
        for (int i=0; i<len; i++){
            temp[i+len]  = nums[i];
        }
        
    return temp; 
    };
};

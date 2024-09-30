int minimumOperations(int* nums, int numsSize) {
        int count = 0; // Initialize the operation counter
        
        // Iterate through each number in the vector
        for (int i = 0; i < numsSize; i++) {
            // Check if either adding or subtracting 1 makes the number divisible by 3
            if (((nums[i] + 1) % 3 == 0) || ((nums[i] - 1) % 3 == 0)) {
                count += 1; // Increment the counter if the condition is met
            }
        }
        return count; // Return the total count of operations needed
}
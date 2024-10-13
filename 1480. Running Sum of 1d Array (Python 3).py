class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the running sums
        l = []
        
        # Loop through the indices of the input list 'nums'
        for i in range(len(nums)):
            # Calculate the sum of elements from the start of 'nums' to the current index 'i'
            count = sum(nums[0:i+1])
            
            # Append the calculated sum to the list 'l'
            l.append(count)

        return l

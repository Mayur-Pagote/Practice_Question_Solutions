class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Perform the operation k times
        for i in range(k):
            # Find the minimum value and its index
            value = min(nums)
            ind = nums.index(value)
            # Update the minimum value by multiplying it
            nums[ind] = value * multiplier
        # Return the modified list
        return nums

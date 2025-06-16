class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        length = len(nums)
        for i in range (length):
            for j in range (i+1, length):
                if nums[i] < nums[j] and i < j:
                    max_diff = max(nums[j] - nums[i], max_diff)
        return max_diff

        

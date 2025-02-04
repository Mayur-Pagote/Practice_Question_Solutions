class Solution(object):
    def maxAdjacentDistance(self, nums):
        nums.append(nums[0])
        max_count = 0
        for i in range(len(nums) - 1):
            max_count = max(max_count, abs(nums[i] - nums[i+1]))
        return max_count

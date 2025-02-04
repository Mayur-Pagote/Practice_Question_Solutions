class Solution(object):
    def countPartitions(self, nums):
        n = len(nums)
        count = 0
        for i in range(n-1):
            left = nums[:i+1]
            right = nums[i+1:]
            if (sum(left) - sum(right)) % 2 == 0:
                count += 1
        return count

class Solution(object):
    def maximumTripletValue(self, nums):
        value = 0
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                for k in range(j ,len(nums)):
                    if i != j and j != k and i != k:
                        value = max(value, (nums[i] - nums[j])*nums[k])
        return value

class Solution(object):
    def check(self, nums):
        arr = nums[:]
        nums.sort()
        
        for i in range(len(nums)):
            s_val = arr[0]
            arr.pop(0)
            arr.append(s_val)
            if arr == nums:
                return True
        return False

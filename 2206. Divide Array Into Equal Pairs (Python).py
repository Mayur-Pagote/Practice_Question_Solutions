class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        set_l = set(nums)
        for i in set_l:
            if nums.count(i) % 2 != 0:
                return False
        return True

        

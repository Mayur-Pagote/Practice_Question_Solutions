class Solution(object):
    def xorAllNums(self, nums1, nums2):
        res = 0

        if len(nums2) % 2 == 1:
            for n in nums1:
                res ^= n

        if len(nums1) % 2 == 1:
            for n in nums2:
                res ^= n

        return res

""" 
Time Limit Exceeded
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        count = 0
        for i in nums1:
            for j in nums2:
                count = count ^ (i^j)
        
        return count
"""

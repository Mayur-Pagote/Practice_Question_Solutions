class Solution(object):
    def twoSum(self, nums, target):

        n = len(nums)  #Storing length of nums.
        index_list = []  #An empty list to store index of nums if target matches.

        #Iterating through nums list.
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    index_list.extend([i,j])

        return index_list

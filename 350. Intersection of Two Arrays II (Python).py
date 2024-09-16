class Solution(object):
    def intersect(self, nums1, nums2):
        temp_list = []
        
        # Iterate over each element in the first list
        for i in nums1:
            if i in nums2:
                temp_list.append(i)
                nums2.remove(i)
        
        return temp_list

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp_list = []
        
        # Iterate over each element in the first list
        for i in nums1:
            if i in nums2:
                temp_list.append(i)
                nums2.remove(i)
        
        return temp_list

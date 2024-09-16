class Solution(object):
    def intersection(self, nums1, nums2):
        # Convert both input lists into sets to remove duplicates and allow fast lookup
        nums1 = set(nums1)
        nums2 = set(nums2)

        temp_list = []

        # Loop through the elements in nums1 set
        for i in nums1:
            # Check if the current element is also in the nums2 set
            if i in nums2:
                temp_list.append(i)

        return temp_list

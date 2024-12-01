class Solution(object):
    def checkIfExist(self, arr):
        for i in arr:
            # If the element is 0 and there is only one 0 in the array, skip this iteration
            if i == 0 and arr.count(0) == 1:
                continue
            # If 'i * 2' exists in the array, return True
            elif i * 2 in arr:
                return True
        # If no condition satisfies, return False
        return False

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num = 0
        for i in set(arr):
            if i == arr.count(i):
                num = max(num, i)
        if num == 0:
            return -1
        else:
            return num

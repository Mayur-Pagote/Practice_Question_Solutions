class Solution(object):
    def pivotArray(self, nums, pivot):
        ll = []
        ml = []
        rl = []
        for i in nums:
            if i < pivot:
                ll.append(i)
            elif i == pivot:
                ml.append(pivot)
            else:
                rl.append(i)
        return ll + ml + rl

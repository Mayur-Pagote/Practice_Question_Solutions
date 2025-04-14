class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        l = len(arr)
        count = 0
        for i in range(l):
            for j in range(i, l):
                for k in range(j, l):
                    if i<j and j<k and k<l:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count +=1
        return count
        

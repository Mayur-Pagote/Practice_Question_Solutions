class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = "aeiou"
        l = []
        count_arr = [0]
        count = 0
        for i in words:
            if i[0] in vow and i[-1] in vow:
                count += 1
                count_arr.append(count)
            else:
                count_arr.append(count)
        
        for m,n in queries:
            l.append(count_arr[n+1] - count_arr[m])
        
        return l

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0

        for i in grid:
            ind = -1
            while True:
                if len(i) < -1*(ind) or i[ind] >= 0:
                    break
                else:
                    count += 1
                    ind -= 1
        return count

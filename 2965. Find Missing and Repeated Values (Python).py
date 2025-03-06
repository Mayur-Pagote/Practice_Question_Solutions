class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        length = len(grid)
        max_ele = length * length 
        l = []
        rep = -1 
     
        for i in range(length):
            for j in range(length):
                l.append(grid[i][j])
                if l.count(grid[i][j]) == 2:  
                    rep = grid[i][j]
        
        for i in range(1, max_ele + 1):
            if i not in l:
                return [rep, i]  

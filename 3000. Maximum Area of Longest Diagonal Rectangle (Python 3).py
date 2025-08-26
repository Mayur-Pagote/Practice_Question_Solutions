class Solution: 
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_sq = 0
        max_area = 0
        
        for length, width in dimensions:
            diagonal_sq = length * length + width * width
            area = length * width
            
            if diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = diagonal_sq
                max_area = area
            elif diagonal_sq == max_diagonal_sq:
                max_area = max(max_area, area)
                
        return max_area

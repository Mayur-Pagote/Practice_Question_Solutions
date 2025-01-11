class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        odd = 0
        s_str = set(s)
        for i in s_str:
            if s.count(i) % 2 != 0:
                odd+=1
        if odd <= k:
            return True
        else:
            return False
        

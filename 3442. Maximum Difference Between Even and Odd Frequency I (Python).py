class Solution(object):
    def maxDifference(self, s):
        s_set = set(s)
        m_odd = -float('inf')  
        m_even = float('inf')  

        for i in s_set:
            count = s.count(i)
            if count % 2 == 0:
                m_even = min(m_even, count)  
            else:
                m_odd = max(m_odd, count)

        return m_odd - m_even if m_even != float('inf') else -1

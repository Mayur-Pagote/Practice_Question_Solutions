class Solution(object):
    def minimumLength(self, s):
        count = 0
        set_s = set(s)
        for i in set_s:
            if s.count(i) % 2 == 0:
                count += 2
            else:
                count += 1
        return count

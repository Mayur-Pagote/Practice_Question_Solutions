class Solution(object):
    def stringMatching(self, words):
        l = []
        for i in words:
            for j in words:
                if i in j and i != j:
                    l.append(i)
                    break
        return l

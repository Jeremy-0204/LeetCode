class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = Counter(s)
        for k, v in s1.items():
            if v == 1:
                return s.index(k)
        return -1
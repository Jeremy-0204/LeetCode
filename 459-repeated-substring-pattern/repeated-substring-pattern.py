class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # n = len(s)

        # for i in range(1, n // 2 + 1):
        #     if n % i == 0:
        #         sub = s[:i]
        #         if sub * (n // i) == s: return True
        # return False

        return s in (s + s)[1:-1]


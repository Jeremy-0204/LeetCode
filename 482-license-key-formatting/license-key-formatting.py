class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split("-")
        s = "".join(c for c in s)
        s = s[::-1]
        result = ""

        for i in range(len(s)):
            result += s[i].upper()
            if i+1 < len(s) and (i+1) % k == 0:
                result += "-"
        
        return result[::-1]

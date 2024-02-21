class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        idx = 0

        for char in t:
            if char == s[idx]:
                idx += 1
            if idx == len(s):
                return True
        
        return False

        # idxs, idxt = 0, 0
        # flag = 0

        # while idxs < len(s) and idxt < len(t):
        #     if s[idxs] == t[idxt]:
        #         idxs += 1
        #         idxt += 1
        #         flag = 1
            
        #     elif ord(s[idxs]) > ord(t[idxt]):
        #         return False
            
        #     else:
        #         idxt += 1
        # if flag == 1: return True
        # else: return False


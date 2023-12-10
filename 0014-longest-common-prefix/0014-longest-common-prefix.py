class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        prefix = strs[0]
        
        for word in strs[1:]:
            while word[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
                
            if not prefix: break
                
        result = str(prefix)
        return result
            
            
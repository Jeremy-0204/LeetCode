class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[': stack.append(c)
            else:
                if c == ')' and len(stack) > 0 and stack[-1] == '(': stack.pop()
                elif c == '}' and len(stack) > 0 and stack[-1] == '{': stack.pop()
                elif c == ']' and len(stack) > 0 and stack[-1] == '[': stack.pop()
                else: return False
        
        if len(stack) > 0: return False
        return True
                
                
class Solution:
    def mySqrt(self, x: int) -> int:
        x1 = float(10 ** ((len(str(x)) + 1) // 2))
        
        while int(x1 * x1) > x:
            x1 = (x1 + x / x1) / 2
            
        return int(x1)
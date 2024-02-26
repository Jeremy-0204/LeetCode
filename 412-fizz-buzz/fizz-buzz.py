class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        dp = {}

        for i in range(1, n+1):
            if i % 3 == 0:
                dp[i] = "Fizz"
            elif i % 5 == 0:
                dp[i] = "Buzz"
            else:
                dp[i] = str(i)
            
            if i % 3 == 0 and i % 5 == 0:
                dp[i] = "FizzBuzz"
        
        return list(dp.values())
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 최솟값 찾기
#         # 최솟값 인덱스 이후로 최댓값 찾기
#         # 만약 최솟값이 맨 뒤에 있으면 최댓값 리턴
        
#         min_idx = prices.index(min(prices))
#         if min_idx == len(prices) - 1 and prices: 
#             return 0
        
#         if max(prices)
#         else:
#             return max(prices[min_idx:]) - min(prices)
                
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buy_price = prices[0]
4        profit = 0
5
6        for p in prices[1:]:
7            if buy_price > p:
8                buy_price = p
9            
10            profit = max(profit, p - buy_price)
11        
12        return profit
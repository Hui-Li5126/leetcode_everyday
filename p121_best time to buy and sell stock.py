You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

>>> class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if max < prices[i] - min:
                max = prices[i] - min
        
        return max


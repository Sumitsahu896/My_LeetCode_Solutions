class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min = 7, max = 7
        min = prices[0]
        max = prices[0]
        
        profit = 0
        
        for price in prices[1:]:
            # min = 1, max = 1 |
            if price < min:
                min = price
                max = price
            # max = 5, profit = 5 - 1 = 4
            elif price > max:
                max = price
                profit = max - min if max - min > profit else profit
                
        return profit
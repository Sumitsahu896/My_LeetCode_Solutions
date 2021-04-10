class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min = prices[0]
        max = prices[0]
        
        profit =  0
        
        for price in prices[1:]:
            
            if price < min:
                min = price
                max = price
                continue
                
            elif price > max:
                max = price
                profit = max - min if max - min > profit else profit
                    
        return profit
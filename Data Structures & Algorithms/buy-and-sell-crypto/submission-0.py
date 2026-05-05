class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('infinity')

        maxprof = 0

        for price in prices:
            if price < minprice:
                minprice = price
            
            prof = price - minprice
            maxprof = max(maxprof, prof)
        
        return maxprof
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_p = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_p:
                max_p = price - min_price
        return max_p
                
        
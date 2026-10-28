class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i, j, n = 0, 1, len(prices)

        if len(prices) <= 1:
            return 0
        
        maxP = 0
        while j < n:
            profit = prices[j] - prices[i]
            if profit >= maxP:
                maxP = profit
            elif prices[j] <= prices[i]:
                i = j
            
            j+=1
        
        return maxP

            
            
        
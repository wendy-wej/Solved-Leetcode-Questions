class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #using two pointers
        l = 0
        r = 1
        
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit) #this stores the greatest
            else:
                l = r #moves l one place to the right
            r += 1 
        return max_profit
    
    

        
        
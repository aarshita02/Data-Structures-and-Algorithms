""" 
Multiple Solutions
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = max(prices)
        maxprofit = 0
        for i in range(len(prices)):
            if (prices[i] < minprice):
                minprice = prices[i];
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice;
        return maxprofit
    
class Solution:
    def maxProfit(self,prices):
        lowest_day = prices[0]
        max_diff = 0
        for price in prices:
            if price < lowest_day:
                lowest_day = price
            diff = price - lowest_day
            if diff > max_diff:
                max_diff = diff
                    
        return max_diff
    
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
      
"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

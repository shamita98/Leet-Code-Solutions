# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell = 0
        profit = 0

        for i in range(1,len(prices)):
            if prices[i]-buy>profit:
                sell=prices[i]
                profit=sell-buy
            elif prices[i]<buy:
                buy=prices[i]
        
        return profit

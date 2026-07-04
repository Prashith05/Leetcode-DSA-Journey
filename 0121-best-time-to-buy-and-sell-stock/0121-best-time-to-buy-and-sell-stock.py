class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # buy=prices[0]
        # sell=0
        # x=0
        # y=0

        # for i in range(len(prices)):
        #     if buy > prices[i]:
        #         buy = prices[i]
        #         x = i
        # for j in range(x, len(prices)):
        #     if sell < prices[j]:
        #         sell=prices[j]
        #         y = j

        # return prices[y]-prices[x]


        buy=prices[0]
        profit=0

        for price in prices:
            if buy > price:
                buy = price
            profit = max(profit, price - buy)
        return profit


        

            
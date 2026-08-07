class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost=prices[0]
        maxprofit=0
        profit=0
        for i in range(len(prices)):
            mincost=min(mincost,prices[i])
            if prices[i]>mincost:
                profit=prices[i]-mincost
            maxprofit=max(maxprofit,profit)
        return maxprofit        
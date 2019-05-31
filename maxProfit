class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        bestCP=prices[0]
        bestProfit=0
        for i in range(len(prices)):
            if(prices[i]<bestCP):
                bestCP=prices[i]
            elif(prices[i]-bestCP > bestProfit):
                bestProfit=prices[i]-bestCP
        return bestProfit
            

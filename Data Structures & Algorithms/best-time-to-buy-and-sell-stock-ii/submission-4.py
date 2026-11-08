class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        bought = False
        profit = 0
        for i in range(len(prices) - 1):
            if bought:
                if prices[i + 1] > prices[i]:
                    continue
                
                if prices[i] > curr:
                    profit += prices[i] - curr
                    bought = False

            else:
                if prices[i + 1] > prices[i]:
                    curr = prices[i]
                    bought = True

        if bought:
            profit += prices[-1] - curr
            
        return profit


                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(prices) - 1:
            if prices[r] >= prices[l]:
                res = max(res, prices[r] - prices[l])
                r += 1
            else:
                l = r

        return max(res, prices[r] - prices[l])
        
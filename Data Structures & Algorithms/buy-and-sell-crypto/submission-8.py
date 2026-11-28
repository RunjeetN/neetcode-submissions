class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return max profit > int
        # sliding window-ish
        # len(prices) >= 2 

        # [10,1,5,6,5 7,1]

        l, r = 0, 1
        res = 0 

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1 
        return res 
        




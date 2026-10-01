class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_price = 1000000
        for price in prices:
            if price < best_price:
                best_price = price
            else:
                profit2 = price - best_price
                if profit2 > profit:
                    profit = profit2
        return profit

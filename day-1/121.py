"""
121. Best Time to Buy and Sell Stock
"""

import math
class Solution:
    def maxProfit(self, prices):
        min_till_now = math.inf
        best_profit = 0
        for price in prices:
            if min_till_now > price:
                min_till_now = price
            elif best_profit < price - min_till_now:
                best_profit = price - min_till_now
        return best_profit

sol1 = Solution()
print(sol1.maxProfit([7,1,5,3,6,4]))
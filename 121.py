class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: return 0
        profit = 0
        save = prices[0]
        sell = prices[0]
        prices[0] = 0
        for i in range(1,len(prices)):
            if prices[i]-save <= 0:
                diff = prices[i] - save
                save = prices[i]
                prices[i] = max(prices[i-1]+diff, 0)
            else:
                temp = prices[i-1] + prices[i] - save
                if temp > profit:
                    profit = temp
                    sell = prices[i] 
                save = prices[i]
                prices[i] = temp
        return profit


# Runtime: 76 ms, faster than 49.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.9 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnum = 10000
        maxprof = 0
        for i in range(len(prices)):
            if prices[i] < minnum:
                minnum = prices[i]
            else:
                if prices[i] - minnum > maxprof:
                    maxprof = prices[i] - minnum
        return maxprof


#Runtime: 76 ms, faster than 49.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 14.7 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.



"""
public class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}
"""
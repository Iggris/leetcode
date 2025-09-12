class Solution(object):
    def maxIceCream(self, costs, coins):
        count = [0] * (max(costs) + 1)
        
        for cost in costs:
            count[cost] += 1
        
        bars = 0

        for price in range(1,len(count)):
            if count[price]>0:
                canbuy=min(count[price],coins//price)
                bars+=canbuy
                coins-=canbuy*price
                if coins==0:
                    break
        return bars

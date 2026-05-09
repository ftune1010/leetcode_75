def maxProfit(prices: list[int], fee: int) -> int:
    # profit = 0
    # effective_buy = prices[0]
    # for i in range(1, len(prices)):
    #     profit = max(profit, prices[i] - fee - effective_buy)
    #     effective_buy = min(effective_buy, prices[i] - profit)
    # return profit
    buy, sell = - prices[0] - fee, 0
    for i in range(1, len(prices)):
        buy, sell = max(buy, sell - prices[i] - fee), max(sell, buy + prices[i])
    return sell

if __name__ == "__main__":
    prices, fee = [1,3,2,8,4,9], 2
    print(maxProfit(prices, fee))
    prices, fee = [1,3,7,5,10,3], 3
    print(maxProfit(prices, fee))
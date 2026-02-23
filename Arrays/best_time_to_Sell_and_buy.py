
"""
Best Time to Buy and Sell Stock

Problem:
Given an array prices where prices[i] is the stock price on day i,
find the maximum profit by buying once and selling once.

Approach:
- Track the minimum price seen so far
- At each day, calculate profit if sold today
- Keep updating maximum profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))  
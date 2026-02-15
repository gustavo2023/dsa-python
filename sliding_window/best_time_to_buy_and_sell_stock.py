"""
Problem: Best Time to Buy and Sell Stock
LeetCode URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Description:
You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                current_profit = prices[i] - min_price
                max_profit = max(max_profit, current_profit)

        return max_profit


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test 1: {sol.maxProfit(prices1)} (Expected: 5)")

    # Test Case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test 2: {sol.maxProfit(prices2)} (Expected: 0)")

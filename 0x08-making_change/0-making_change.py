#!/usr/bin/python3
"""
initialisation
"""


def makeChange(coins, total):
    """ Make change function"""

    if total <= 0:
        return 0
    
    # Initialize the dp array with a value greater than any possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

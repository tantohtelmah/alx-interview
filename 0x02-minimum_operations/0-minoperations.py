#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """ function"""

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for d in range(1, i // 2 + 1):
            if i % d == 0:
                dp[i] = min(dp[i], dp[d] + i // d)

    return dp[n]

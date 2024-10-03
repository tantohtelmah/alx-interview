#!/usr/bin/python3
""" Initialisation"""


def isWinner(x, nums):
    """ The winner function"""

    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n):
        """ play game function """

        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            moves = play_game(n)
            if moves % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

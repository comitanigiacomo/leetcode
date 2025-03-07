from typing import List

class Solution:

    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0], sieve[1] = False, False

        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, right + 1, i):
                    sieve[multiple] = False

        primes = [i for i in range(left, right + 1) if sieve[i]]

        if len(primes) < 2:
            return [-1, -1]

        num1, num2 = -1, -1
        min_diff = float('inf')

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                num1, num2 = primes[i], primes[i + 1]

        return [num1, num2] 
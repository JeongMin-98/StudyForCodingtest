import math
import sys

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, sys.stdin.readline().split())

    max_year = m * n // math.gcd(m, n)
    year = -1

    while x <= max_year:
        if (x - y) % n == 0:
            year = x
            break
        x += m

    print(year)
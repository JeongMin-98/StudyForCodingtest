"""

    1 1 2 3 5 8 13 ...

    100번째 fibonacci 수열을 구하라
"""

dp = [0] * 100

# 하향식
# def fibo(num):
#     if num == 1 or num == 2:
#         return 1
#     if dp[num] != 0:
#         return dp[num]
#
#     dp[num] = fibo(num-1) + fibo(num-2)
#     return dp[num]

dp[0] = 1
dp[1] = 2
n = 99
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[99])

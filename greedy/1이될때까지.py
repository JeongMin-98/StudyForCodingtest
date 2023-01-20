"""

    N 과 K가 공백을 기준으로 하여 각각 자연수로 주어진다.

    N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력

    1) N에서 1을 뺍니다.
    2) N을 K로 나눈다.
    2)번은 N % K == 0일떄만 시행 가능




"""


def solution(N, K):
    dp = [0] * (N + 1)

    for i in range(2, N + 1):

        dp[i] = dp[i - 1] + 1

        if i % K == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 4] + 1)

    return dp[N]


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(solution(n, k))

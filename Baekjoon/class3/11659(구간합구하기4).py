"""

    수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

    1 ≤ N ≤ 100,000
    1 ≤ M ≤ 100,000

    첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.

    둘째 줄에는 N개의 수가 주어진다.
    수는 1,000보다 작거나 같은 자연수이다.
    셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.


"""


def cal_i_j(N, number, i, j):
    dp = [0] * (N + 1)

    dp[1] = number[0]

    for x in range(2, j + 1):
        dp[x] = dp[x - 1] + number[x - 1]

    return dp[j] - dp[i - 1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        print(cal_i_j(N, number, i, j))

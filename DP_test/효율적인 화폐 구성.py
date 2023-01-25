"""

    N가지 종류의 화폐가 있다.

    화폐들의 개수를 최소한으로 이용하여

    화폐들의 가치의 합이 M원이 되도록 한다.

    M원을 만들기 위한 최소한의 화폐 개수는?

    N => 주어진 화폐의 종류
    M => 원하고자하는 화폐들의 합

"""

MAX = 10001


def solution(m, money):
    dp = [MAX] * (m + 1)
    # money : 2, 3
    min_base = min(money)
    for i in range(min_base, m + 1):

        if i in money:
            dp[i] = 1
        for base in money:
            dp[i] = min(dp[i], dp[i - base] + 1)

    if dp[m] == MAX:
        return -1
    return dp[m]


if __name__ == '__main__':
    n, m = map(int, input().split())
    money = []
    for _ in range(n):
        money.append(int(input()))

    print(solution(m, money))

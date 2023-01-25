"""

    정수 X가 주어졌을 때 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

    X가 5로 나누어 떨어지면, 5로 나눈다.
    X가 3으로 나누어 떨어지면, 3으로 나눈다.
    X가 2로 나누어 떨어지면 2로 나눈다.
    X에서 1을 뺀다.

"""


def solution(X):
    dp = [0] * (X + 1)

    for i in range(2, X + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    return dp[X]


if __name__ == '__main__':
    X = int(input())
    print(solution(X))

"""

    [BAEKJOON] https://www.acmicpc.net/problem/9095

    1,2,3의 합으로 나타내는 방법
    합을 나타낼 때는 수를 1개 이상 사용해야함

    정수 n n은 양수이며 11보다 작다



"""


def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return dp(n - 1) + dp(n - 2) + dp(n - 3)


if __name__ == '__main__':

    T = int(input())
    for _ in range(T):
        print(dp(int(input())))

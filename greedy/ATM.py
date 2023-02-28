"""

    [Baekjoon] https://www.acmicpc.net/problem/11399

    1번부터 N번까지 번호가 매겨져 있으며,
    i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분

    p1 = 3
    p2 = 1
    p3 = 4
    p4 = 3
    p5 = 2

    p2 p5 p4 p1 p3

"""
import sys

sys.setrecursionlimit(1001)


def dp(n):
    global dp_times
    global times
    if n == 0:
        dp_times[0] = times[0]
        return dp_times[0]
    dp_times[n] = dp(n - 1) + times[n]
    return dp_times[n]


if __name__ == '__main__':
    T = int(input())

    times = list(map(int, input().split()))
    # print(sys.getrecursionlimit())
    times = sorted(times)
    dp_times = [0] * T
    answer = 0
    for i in range(len(times)):
        answer += sum(times[:i+1])
    dp(T - 1)

    print(sum(dp_times))
    # print(answer)
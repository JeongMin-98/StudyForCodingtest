"""

    n * m 크기의 금광

    특정한 크기의 금이 들어가 있다.

    채굴자는 첫번째 열부터 출발하여 금을 캐기 시작

    맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.

    m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽 아래 3가지 중 하나의 위치로 이동해야함

    오른쪽 위, 오른쪽 오른쪽 아래

    각각의 행렬에서 시작해서 구해야함.

    오른쪽 위 4
    오른쪽 3
    오른쪽 아래 2

    m번째 열에 속한다면 --> 3m < idx < 3m+2 --> 0 <= idx <= 2
    m+1번째로 이동하여 해당 범위안에 있어야함 --> 3(m+1) <= idx <= 3(m+1)+2 --> 3 <= idx <= 5

    1 3 3 [ 0 1 2 ]
    2 2 1 [ 3 4 5 ]
    4 1 0 [ 6 7 8 ]
    6 4 7 [ 9 10 11]

"""

from collections import defaultdict


def in_boundary(i, loc, n):
    start = ((i // n) - 1) * 3
    end = start + n
    if start <= loc < end:
        return True
    return False


def solution(n, m, mine):
    dp = [0] * n * m

    direction = [n + 1, n, n - 1]
    dp[0:n] = mine[0:n]

    for i in range(n, n * m):
        for d in direction:
            before = i - d
            if in_boundary(i, before, n):
                dp[i] = max(dp[i], dp[before] + mine[i])

    max_mine_idx = n * m
    last_line_start_idx = n * (m - 1)
    return max(dp[last_line_start_idx: max_mine_idx])


if __name__ == '__main__':

    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))

        print(solution(n, m, arr))
    print('end')

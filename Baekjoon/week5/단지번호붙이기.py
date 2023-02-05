"""

    Baekjoon: https://www.acmicpc.net/problem/2667

    정사각형 모양의 지도가 있다.

    1은 집이 있는 곳
    0은 집이 없는 곳

    지도에서 연결된 집의 모임을 단지로 정의하고, 단지에 번호를 붙이려 한다.

    여기서 연결되었다라는 의미는 어떤 집이 좌우 혹은 아래위로 다른 집이 있는 경우를 말한다.
    대각선상에 집이 있는 경우는 연결된것이 아니다.

    만들어지는 단지의 총 개수와
    각 단지내 집의 개수를 출력

"""
from collections import deque
from heapq import *


def dfs(arr, y_idx, x_idx):
    global N
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append([y_idx, x_idx])
    arr[y_idx][x_idx] = 0
    cnt = 1
    while queue:
        y, x = queue.pop()
        for ny, nx in zip(dy, dx):
            ty = y + ny
            tx = x + nx
            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue
            if arr[ty][tx] == 1:
                arr[ty][tx] = 0
                cnt += 1
                queue.append([ty, tx])

    return cnt


def solve(arr, N):
    """ 순서대로 이동할 방향"""

    visited = [[0] * N for _ in range(N)]
    """ arr를 0, 0부터 차례대로 방문"""
    town = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                heappush(town, dfs(arr, y, x))
    return town


if __name__ == '__main__':

    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(list(map(int, input())))
    count = solve(grid, N)

    print(len(count))
    for _ in range(len(count)):
        print(f'{heappop(count)}')

"""

    Baekjoon: https://www.acmicpc.net/problem/2178

    N * M 크기의 배열로 표현되는 미로

    미로에서 1은 이동할 수 있는 칸
    0은 이동할 수 없는 칸

    (1,1)에서 출발해 (N,M)의 위치로 이동할 때 지나야하는 최소의 칸 수

    서로 인접한 칸으로만 이동 가능

"""

from collections import deque


def solve():
    """ 미로 탐색 """

    global array
    queue = deque([[0, 0]])

    x = [0, 1, -1, 0]
    y = [1, 0, 0, -1]

    while len(queue) > 0:
        cur_x, cur_y = queue.popleft()
        for dx, dy in zip(x, y):
            temp_x = cur_x + dx
            temp_y = cur_y + dy
            if 0 > temp_x or temp_x >= M or 0 > temp_y or temp_y >= N:
                continue
            if array[temp_y][temp_x] == 0:
                continue
            if array[temp_y][temp_x] == 1:
                array[temp_y][temp_x] = array[cur_y][cur_x] + 1
                queue.append([temp_x, temp_y])


if __name__ == '__main__':
    N, M = map(int, input().split())

    array = []
    for _ in range(N):
        array.append(list(map(int, input())))
    solve()
    print(array[N - 1][M - 1])

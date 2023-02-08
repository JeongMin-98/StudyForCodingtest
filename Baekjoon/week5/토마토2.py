"""

    익은 토마토는 익지 않은 토마토들을 익게 한다.

    인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯방향이다.

    대각선 방향에 있는 토마토들에게는 영향을 주지 못함. 혼자 저절로 익는 경우는 없다.

    창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어한다.

    격자 모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어진다.

    며칠이 지나면 토마토들이 모두 익는지 그 최소 일수를 구하는 프로그램을 작성해라

    일부 칸에는 토마토가 들어있지 않을 수도 있다.

    상자의 크기 M(가로), N(세로) 과 상자의 수 H가 주어짐

    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [1, -1, 0, 0, 0, 0]

"""
from collections import deque
import sys


def dfs(m, n, box, q):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    day = 0

    while q:
        ty, tx = q.popleft()

        for x, y in zip(dx, dy):
            ny = ty + y
            nx = tx + x

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if box[ny][nx] == -1:
                continue

            if box[ny][nx] >= 1:
                continue

            q.append([ny, nx])
            box[ny][nx] = box[ty][tx] + 1

    for i in box:
        if 0 in i:
            return -1
        for j in i:
            day = max(day, j)

    return day - 1


if __name__ == '__main__':

    M, N = map(int, input().split())
    queue = deque()
    box = []
    for yi in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))
        for xi in range(M):
            if box[yi][xi] == 1:
                queue.append([yi, xi])

    print(dfs(M, N, box, queue))

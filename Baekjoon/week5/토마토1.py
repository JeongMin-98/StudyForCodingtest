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

def solution(m, n, h, boxes, q):
    total = m * n * h
    day = -1
    # direction
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [1, -1, 0, 0, 0, 0]  # h의 vector는 z로 나타냄

    while q:
        th, ty, tx = q.popleft()

        for x, y, z in zip(dx, dy, dh):
            nh = th + z
            ny = ty + y
            nx = tx + x

            if nx < 0 or nx >= m or ny < 0 or ny >= n or nh < 0 or nh >= h:
                continue

            if boxes[nh][ny][nx] == -1:
                continue

            if boxes[nh][ny][nx] >= 1:
                continue

            q.append([nh, ny, nx])
            boxes[nh][ny][nx] = boxes[th][ty][tx] + 1

    for i in boxes:
        for j in i:
            if 0 in j:
                return -1
            day = max(day, max(j))
    return day-1


if __name__ == '__main__':

    M, N, H = map(int, input().split())
    graph = []
    queue = deque()
    for hi in range(H):
        box = []
        for yi in range(N):
            box.append(list(map(int, sys.stdin.readline().split())))
            for xi in range(M):
                if box[yi][xi] == 1:
                    queue.append([hi, yi, xi])
        graph.append(box)

    print(solution(M, N, H, graph, queue))

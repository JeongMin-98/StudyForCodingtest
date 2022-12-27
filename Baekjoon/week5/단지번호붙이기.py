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

def solve(arr, N):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    apart_name = 1
    visited = [[0] * N for _ in range(N)]
    trival = deque([])
    for y_i, x_values in enumerate(arr):
        for x_i, value in enumerate(x_values):
            if not visited[y_i][x_i] and arr[y_i][x_i] == 1:
                visited[y_i][x_i] = 1
                trival.append([y_i, x_i])

                while trival:
                    cur_y, cur_x = trival.popleft()

                    for x, y in zip(dx, dy):
                        ny = cur_y+y
                        nx = cur_x+x
                        if visited[ny][nx]:
                            continue
                        if arr[ny][nx] == 0:
                            continue
                        if 0 > ny or ny >= N or 0 > nx or nx >= N:
                            continue

                        visited[ny][nx] = 1
                        arr[ny][nx] = apart_name
                        trival.append([ny, nx])




    return




if __name__ == '__main__':

    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(map(int, input().split()))

    solve()

"""

    n: 세로의 크기
    m: 가로의 크기

"""
import sys

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def is_in_map(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    return False


def bfs(i, j, n, m, visited, grid):
    queue = []

    visited[i][j] = 1
    grid[i][j] = 0

    queue = [[i, j]]

    while queue:

        cur_i, cur_j = queue.pop(0)
        for i_, j_ in zip(di, dj):
            next_i = cur_i + i_
            next_j = cur_j + j_

            if is_in_map(next_i, next_j, n, m) and not visited[next_i][next_j] and grid[next_i][next_j] == 1:
                visited[next_i][next_j] = 1
                board[next_i][next_j] = board[cur_i][cur_j] + 1
                queue.append([next_i, next_j])


if __name__ == '__main__':
    n, m = map(int, input().split())

    visited = [[0] * m for _ in range(n)]
    board = [[-1] * m for _ in range(n)]
    grid = []
    tar_i, tar_j = None, None
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if temp[j] == 2:
                tar_i, tar_j = i, j
                board[tar_i][tar_j] = 0

            if temp[j] == 0:
                board[i][j] = 0
        grid.append(temp)

    bfs(tar_i, tar_j, n, m, visited, grid)

    for i in range(n):
        for j in range(m):
            print(board[i][j], end=" ")
        print()

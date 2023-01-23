"""

    N * M 크기의 얼음 틀이 있다.

    구멍이 뚫려 있는 부분 0
    칸막이가 존재하는 부분 1

    상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주

"""


def solution(ice, N, M):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                continue

            queue = [[i, j]]
            while queue:
                temp_y, temp_x = queue.pop(0)
                ice[temp_y][temp_x] = 1
                for x, y in zip(dx, dy):
                    next_x = temp_x + x
                    next_y = temp_y + y

                    if next_y < 0 or next_y >= N or next_x < 0 or next_x >= M:
                        continue

                    if ice[next_y][next_x]:
                        continue

                    if [next_y, next_x] not in queue:
                        queue.append([next_y, next_x])

            cnt += 1

    return cnt


if __name__ == '__main__':

    N, M = map(int, input().split(' '))

    ice = []
    for _ in range(N):
        ice.append(list(map(int, input())))

    graph = ice.copy()

    print(f"{solution(ice, N, M)}")

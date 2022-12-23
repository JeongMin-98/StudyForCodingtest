"""

    Baekjoon: https://www.acmicpc.net/problem/1992

    쿼드 트리는 흑백영상을 압축하여 표현하는 데이터 구조

    흰점은 0
    검은점은 1

    영상의 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나눠 압축 한다.

"""
import math
import sys


def insert(src, line, pos):
    return ''.join([src[:pos], line, src[pos:]])


def split(array, size, x0, x1, y0, y1):
    """ array => 영상의 데이터 배열, size는 영상의 크기 ex) 8 = 2**3 size=3 """
    if math.log2(size) > 1:
        size = size // 2
        x_mid = x0 + size
        y_mid = y0 + size

        lu = split(array, size, x0, x_mid - 1, y0, y_mid - 1)  # 왼쪽 위
        ru = split(array, size, x0, x_mid - 1, y_mid, y1)  # 오른쪽 위
        ld = split(array, size, x_mid, x1, y0, y_mid - 1)  # 왼쪽 아래
        rd = split(array, size, x_mid, x1, y_mid, y1)  # 오른쪽 아래

    else:
        area_value = set([array[x0][y0], array[x0][y1], array[x1][y0], array[x1][y1]])

        if len(area_value) == 1:
            area_value = list(area_value)
            return str(area_value[0])
        else:
            return f'({array[x0][y0]}{array[x0][y1]}{array[x1][y0]}{array[x1][y1]})'
    if lu is None and ru is None and ld is None and rd is None:
        return

    result = [lu, ru, ld, rd]
    count_one = result.count('1')
    count_zero = result.count('0')

    if count_one == 4:
        return lu

    if count_zero == 4:
        return lu

    merge = '()'
    for r in result:
        merge = insert(merge, r, -1)

    return merge


if __name__ == '__main__':
    N = int(input())
    video = [list(map(int, input())) for _ in range(N)]

    area = split(video, N, 0, N - 1, 0, N - 1)
    print(area)

"""

    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있음

    수열에서 x가 등장하는 횟수를 계산

    수열 {1, 1, 2, 2, 2, 2, 3}
    num = 2 이기 때문에 원소 4개를 출력

"""

from bisect import *


def solution(arr, x, N):
    left_idx = bisect_left(arr, x)
    right_idx = bisect_right(arr, x)
    cnt = right_idx - left_idx
    if cnt > 0:
        return cnt
    return -1


if __name__ == '__main__':
    N, x = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution(arr, x, N))

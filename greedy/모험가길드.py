"""

    모험가 N 명이 있다.

    모험가는 각자 공포도를 가진다.

    공포도는 높을 수록 위험 상황에서 제대로 대처할 능력이 떨어진다.

    공포도가 X인 모험가는 X명 이상으로 모험가 그룹을 만들어야 여행을 떠날 수 있다.

    최대 몇 개의 모험가 그룹을 만들 수 있는지

    공포도가 모두 최저가 되도록 만들어야함

    5
    2 3 1 2 2

    3 2 1
    2 2

"""


def solution(n, arr):
    group = []
    cnt = 0
    arr.sort(reverse=True)
    while arr:
        group.append(arr.pop(0))
        if not arr:
            break

        group_len = group[0] - 1

        for _ in range(group_len):
            group.append(arr.pop(-1))

        group = []
        cnt += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    fears = list(map(int, input().split(' ')))

    print(solution(n, fears))

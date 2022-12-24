"""

    Baekjoon: https://www.acmicpc.net/problem/2578

    각각의 계단에는 일정한 점수가 쓰여져 있다
    계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

    규칙
    1. 계단은 한 번에 한 계단 or 두 계단씩 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. / 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.

"""
from collections import deque


def on_stair(temp, cnt_of_stair):
    if temp < cnt_of_stair:
        return True
    else:
        return False


def solve(stair_info, temp_score, cnt_of_stair):
    i = -1
    step_one = 0

    step = deque()
    step.append([i, step_one])

    score = 0
    while len(step) > 0:
        temp, step_one = step.popleft()
        if temp == -1:
            temp_score[temp + 1] = stair_info[temp + 1]
            temp_score[temp + 2] = stair_info[temp + 2]
            step.append([temp + 1, step_one + 1])
            step.append([temp + 2, step_one])
            continue
        if on_stair(temp + 1, cnt_of_stair):
            if step_one > 3:
                continue
            if temp_score[temp + 1] > (temp_score[temp + 1] + stair_info[temp]):
                continue

            step.append([temp + 1, step_one + 1])
            temp_score[temp + 1] += stair_info[temp]

        if on_stair(temp + 2, cnt_of_stair):
            if temp_score[temp + 2] > (temp_score[temp + 2] + stair_info[temp]):
                continue

            step.append([temp + 2, 0])
            temp_score[temp + 2] += stair_info[temp]

    return temp_score[cnt_of_stair - 1]


if __name__ == '__main__':

    N = int(input())
    stair = []
    for _ in range(N):
        stair.append(int(input()))

    temp_stair = [0] * N

    print(solve(stair, temp_stair, N))

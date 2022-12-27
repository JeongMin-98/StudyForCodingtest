"""

    Baekjoon: https://www.acmicpc.net/problem/2578

    각각의 계단에는 일정한 점수가 쓰여져 있다
    계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

    규칙
    1. 계단은 한 번에 한 계단 or 두 계단씩 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. / 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.

"""


def solve(stair, cnt_of_stair):
    stair_score = []

    if cnt_of_stair == 1:
        return stair[0]

    if cnt_of_stair == 2:
        return max(stair[1], stair[1] + stair[0])

    stair_score.append(stair[0])
    stair_score.append(max(stair[0] + stair[1], stair[1]))
    stair_score.append(max(stair[1] + stair[2], stair[0] + stair[2]))

    for i in range(3, cnt_of_stair):
        stair_score.append(max(stair_score[i - 2] + stair[i], stair_score[i - 3] + stair[i - 1] + stair[i]))

    return stair_score[-1]


if __name__ == '__main__':

    N = int(input())
    stair = []
    for _ in range(N):
        stair.append(int(input()))

    print(solve(stair, N))

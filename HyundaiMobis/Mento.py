from heapq import heappush, heappop
from collections import defaultdict
from itertools import combinations_with_replacement, permutations
from copy import deepcopy


def make_case(k, n):
    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n - k + 2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                cases.add(perm)

    return cases


def sort_req_for_type(reqs):
    # 각 유형별로 분류
    reqs_type = defaultdict(list)
    for req in reqs:
        # 요청시각과 상담 시간을 각 유형별로 분류하기
        reqs_type[req[2]].append([req[0], req[1]])

    return reqs_type


def cal_wait_time(reqs, n):  # 유형 별 waiting_list에 n명의 상담 원이 있을 때 대기 시간 계산
    total_time = 0
    execute = []
    wait = []

    for _ in range(n):
        heappush(execute, 0)

    while reqs or wait:

        # wait queue가 있을 경우
        if wait:
            temp = wait.pop(0)
            temp_wait = temp[2]
        else:
            temp = reqs.pop(0)
            temp_wait = 0

        temp_start = temp[0]
        temp_remain = temp[1]

        # 멘토가 상담할 수 있는 경우
        if execute:
            pop_seat_time = heappop(execute)

        if temp_start >= pop_seat_time:
            end = temp_start + temp_remain
            total_time += temp_wait
            heappush(execute, end)
        # 상담을 할 수 없는 경우
        else:
            heappush(execute, 0)
            wait_time = pop_seat_time - temp_start
            new_start_time = pop_seat_time
            heappush(wait, [new_start_time, temp_remain, wait_time])

        # 상담이 완료되었을 경우 execute queue에서 제외

    return total_time


def solution(k, n, reqs):
    result = 1e9

    # 멘토 유형의 모든 case를 만들기
    cases = make_case(k, n)

    # 각 유형별로 상담 요청 분류하기
    req_for_type = sort_req_for_type(reqs)

    # 상담별로 정해진 스케줄을 통해 대기시간 측정하기
    for case in cases:
        time = 0
        for i in range(1, k + 1):
            time += cal_wait_time(deepcopy(req_for_type[i]), case[i - 1])
        # 무조건 최소시간으로 추출하기
        result = min(result, time)

    return result


# print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))
print(solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1],
                      [70, 100, 2]]))

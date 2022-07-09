"""

    중요도가 높은 문서를 먼저 인쇄하는 프린터

    queue 구조를 활용

        1. 인쇄 대기 목록의 가장 앞에 있는 문서(J)를 대기 목록에서 꺼냅니다.
        2. J보다 나머지 대기 목록에서 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        3. 그렇지 않으면 J를 인쇄합니다.

                                        ------------------
                                        =   A, B, C, D   =
                                        =   2, 1, 3, 2   =
                                        ------------------

        1) A / B C D (2) / C가 우선순위가 더 놓음
        2) C / B D A -> C 인쇄
        3) B / D A -> B보다 높은 우선순위를 가진 인쇄물이 있음
        4) D / A B -> D랑 동급 그래서 D 인쇄
        5) A / B -> A > B A 인쇄
        6) B 인쇄

        C D A B

"""

def solution(priorities, location):
    answer = 0
    orders = [0] * len(priorities)
    cur_loc = 0
    job = []
    for i in range(0, len(priorities)):
        job.append((priorities[i],i))
    print_order = 1
    while len(job) > 0:
        cur_pri, cur_index = job.pop(0)
        if len(job) > 0:
            max_pri, max_index = job[job.index(max(job))]
        else:
            break
        if cur_pri < max_pri:
            job.append((cur_pri, cur_index))
        else:
            orders[cur_index] = print_order
            print_order += 1
        print(orders)

    orders[cur_index] = print_order
    answer = orders[location]
    return answer

print(solution([2, 1, 3, 2], 2))
"""

    start:출발지,
    end: 도착지
    n=> 방의 개수
    roads [1,2,2] => 1 node -> 2 node 걸리는 시간 : 2
    traps = 그 방에 도달하는 루트가 반대 방향으로.

    traps인 방의 root를 구하는 방법은
    roads [1,2,2]  --> [2,1,2]

"""
from queue import PriorityQueue
MAX = 3001

#
# def make_route(n, roads, trap, graph, trap_route):
#
#     for i in range(0, n + 1):
#         graph[i] = []
#         if trap[i] == 1:
#             trap_route[i] = []
#     for road in roads:
#         src = road[0]
#         dst = road[1]
#         time = road[2]
#         if trap[dst] == 1:
#             trap_route[dst].append((src, time))
#         graph[src].append((dst, time))
#     return graph, trap_route
#
#
# def solution(n, start, end, roads, traps):
#
#     answer = 0
#     graph = dict()
#     trap_route = dict()
#
#     trap = [0] * (n + 1)
#     for i in traps:
#         trap[i] = 1
#
#     time = 0
#     wait_select = PriorityQueue()
#     used_route = [[0]*(n+1) for _ in range(0, n+1)]
#     time = [MAX] * (n+1)
#     time[start] = 0
#     graph, trap_route = make_route(n, roads, trap, graph, trap_route)
#     wait_select.put((time[start], start))
#
#     while wait_select.qsize() > 0:
#         current_time, current_src = wait_select.get()
#
#         # if time[current_src] < current_time:
#         #     continue
#         if trap[current_src] == 1:
#             route = trap_route
#         else:
#             route = graph
#         for next_src, next_time in route[current_src]:
#             if used_route[current_src][next_src] == 0:
#                 total_time = current_time + next_time
#                 # if time[next_src] > total_time:
#                 time[next_src] = total_time
#                 used_route[current_src][next_src] = 1
#                 wait_select.put((time[next_src], next_src))
#     print(time)
#     answer = time[end]

from queue import PriorityQueue
MAX = 3001


def make_route(n, roads, trap, graph):

    for i in range(0, n + 1):
        graph[i] = []
    for road in roads:
        src = road[0]
        dst = road[1]
        time = road[2]
        if trap[dst] == 1:
            graph[dst].append((src, time))
        graph[src].append((dst, time))
    return graph


def solution(n, start, end, roads, traps):

    answer = 0
    graph = dict()

    trap = [0] * (n + 1)
    for i in traps:
        trap[i] = 1

    time = 0
    wait_select = PriorityQueue()
    used_route = [[0]*(n+1) for _ in range(0, n+1)]
    time = [MAX] * (n+1)
    time[start] = 0
    graph = make_route(n, roads, trap, graph)
    wait_select.put((time[start], start))

    while wait_select.qsize() > 0:
        current_time, current_src = wait_select.get()
        route = graph
        for next_src, next_time in route[current_src]:

            total_time = current_time + next_time
            time[next_src] = total_time
            if used_route[current_src][next_src] == 0:
                used_route[current_src][next_src] = 1
                wait_select.put((time[next_src], next_src))

    answer = time[end]

    return answer


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
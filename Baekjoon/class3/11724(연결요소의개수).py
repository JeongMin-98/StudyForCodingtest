"""

    방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

    정점의 개수 N과 간선의 개수 M

     둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v

     1,2,5 -> 1 다른 연결 요소에

"""
import sys
from collections import defaultdict

sys.setrecursionlimit(2500)

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(u):
    visited[u] = True
    if u in graph:
        for v in graph[u]:
            if visited[v] == False:
                dfs(v)


visited = [False for _ in range(N + 1)]
count = 0

for u in range(1, N + 1):
    if visited[u] == False:
        dfs(u)
        count += 1

print(count)

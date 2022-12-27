"""

    1 - 2 - 3  4
     \ /       /
      5 - 6    7

    컴퓨터가 윔 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서
    연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하시요

"""
from collections import defaultdict, deque


def solve(tree):
    global N
    temp = deque([1])
    visited = [0] * (N + 1)
    visited[1] = 1
    while temp:
        temp_node = temp.popleft()
        for next_node in tree[temp_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                temp.append(next_node)
    return sum(visited) - 1


if __name__ == '__main__':
    N = int(input())
    V = int(input())
    graph = defaultdict(list)

    """ defaultdict으로 그래프 생성 """
    for _ in range(V):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    print(solve(graph))

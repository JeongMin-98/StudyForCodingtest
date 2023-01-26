def dfs(graph, start, visited):
    visited[start] = 1

    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = dict()

graph[1] = [2, 3, 8]
graph[2] = [1, 7]
graph[3] = [1, 4, 5]
graph[4] = [3, 5]
graph[5] = [3, 4]
graph[6] = [7]
graph[7] = [2, 6, 8]
graph[8] = [1, 7]

v = [0] * 9
dfs(graph, 1, v)

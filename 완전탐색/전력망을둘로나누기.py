
def count_node(node, network):

    cnt = 0
    visited = []
    queue = [node]
    while len(queue) > 0:
        temp = queue.pop(0)
        visited.append(temp)
        cnt += 1
        for next_node in network[temp]:
            if next_node not in visited:
                queue.append(next_node)
    return cnt
def make_network(wires):
    """
        하나의 트리로 이루어져 있다.
        주어진 wires를 입력값으로 받아
        송전선으로 연결된 트리 맵을 dictionary 형태로 return
    """
    network = dict()
    for v1, v2 in wires:
        if v1 not in network.keys():
            network[v1] = [v2]
        else:
            network[v1].append(v2)
        if v2 not in network.keys():
            network[v2] = [v1]
        else:
            network[v2].append(v1)
    return network

def solution(n, wires):

    answer = 1000
    # 트리맵 만들기
    network = make_network(wires)
    # 연결 끊기
    for v1, v2 in wires:
        network[v1].pop(network[v1].index(v2))
        network[v2].pop(network[v2].index(v1))

        a_net = count_node(v1, network)
        b_net = count_node(v2, network)

        if answer >= abs(a_net - b_net):
            answer = abs(a_net - b_net)

        network[v1].append(v2)
        network[v2].append(v1)

    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))
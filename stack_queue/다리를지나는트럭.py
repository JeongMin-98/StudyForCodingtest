"""

    여러 대가 일차선 다리를 정해진 순으로 건넘

    모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는 지

    다리는 최대로 올라갈 수 있는 수 가 정해져있음 -> bridge_length
    다리의 최대 무게 제한 -> weight
    다리에 완전히 오르지 않은 경우 트럭의 무게가 무시됨

    다리를 지난 트럭
    arrived_truck = []
    다리를 지나고 있는 트럭
    pass_truck = []
    대기 트럭
    wait_truck = []

    bridege_length > len(pass_truck) 이어야 pass_truck에 들어갈 수 있음
    즉 다리를 건널 수 있음

"""

def solution(bridge_length, weight, truck_weights):
    answer = 0

    arrived_truck = []
    pass_truck = []
    wait_truck = truck_weights.copy()
    total_truck = len(truck_weights)
    time = 1

    while 1:
        if len(pass_truck) < bridge_length:
            if len(wait_truck) == 0:
                arrived_truck.append(pass_truck.pop(0))
            if sum(pass_truck) < weight:
                pass_truck.append(wait_truck.pop(0))
            else:
                pass
        else:


    return answer

print(solution(2, 10, [7,4,5,6]))
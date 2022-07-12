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

    bridge_length > len(pass_truck) 이어야 pass_truck에 들어갈 수 있음
    즉 다리를 건널 수 있음

    bridge_length 만큼 차가 이동하여 건넌다.
"""
def sum_weight_truck(pass_truck):
    total_weight = 0
    for weight, pass_len in pass_truck:
        total_weight += weight
    return total_weight

def solution(bridge_length, weight, truck_weights):
    answer = 0

    arrived_truck = []
    pass_truck = []
    wait_truck = truck_weights.copy()
    total_truck = len(truck_weights)
    time = 1

    while len(arrived_truck) < total_truck:

        if len(wait_truck) > 0:
            input_truck = wait_truck.pop(0)

        if len(pass_truck) == 0:
            pass_truck.append([input_truck, bridge_length])
        else:
            total_weight = sum_weight_truck(pass_truck) + input_truck
            # 무게 제한에 따른 통행 유무
            weight_limit = total_weight <= weight
            # 다리 위에 있는 트럭의 수에 따른 통행 유무
            on_limit = len(pass_truck) <= bridge_length
            pass_yn = weight_limit and on_limit
            if pass_yn:
                pass_truck.append([input_truck, bridge_length])
            else:
                wait_truck.insert(0, input_truck)
        for i in range(len(pass_truck)):
            pass_truck[i][1] -= 1
        truck_weight, pass_len = pass_truck.pop(0)
        if pass_len == 0:
            arrived_truck.append(truck_weight)
        else:
            pass_truck.insert(0, [truck_weight, pass_len])
        time += 1
        print("time {}, arrived {}, pass {}, wait {}\n".format(time, arrived_truck, pass_truck, wait_truck))

    answer = time
    return answer



print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10,10]))


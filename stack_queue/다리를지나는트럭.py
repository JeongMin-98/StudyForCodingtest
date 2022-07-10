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

def solution(bridge_length, weight, truck_weights):
    answer = 0

    arrived_truck = []
    pass_truck = []
    wait_truck = truck_weights.copy()
    total_truck = len(truck_weights)
    time = 1

    while len(arrived_truck) < total_truck:

        if len(wait_truck) > 0:
            temp = wait_truck.pop(0)
            if len(pass_truck) == 0:
                pass_truck.append(temp)
            else:
                total_pass = sum(pass_truck) + temp
                if total_pass < weight:
                    if len(pass_truck) < bridge_length:
                        pass_truck.append(temp)
                    else:
                        wait_truck.insert(0, temp)
                        arrived_truck.append(pass_truck.pop(0))
                else:
                    wait_truck.insert(0, temp)
                    if len(pass_truck) < bridge_length:
                        time += bridge_length
                        arrived_truck.append(pass_truck.pop(0))
                    else:
                        arrived_truck.append(pass_truck.pop(0))
        else:

        print("time {}, arrived {}, pass {}, wait {}".format(time, arrived_truck, pass_truck, wait_truck))


    answer = time
    return answer

print(solution(2, 10, [7,4,5,6]))
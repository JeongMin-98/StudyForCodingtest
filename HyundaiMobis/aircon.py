"""

    문제 주소: https://school.programmers.co.kr/learn/courses/30/lessons/214289?language=python3

    승객이 탑승 중일 때 항상 쾌적한 실내온도 t1 ~ t2를 유지할 수 있도록 한다.

    현재(0분) 실내온도는 실외 온도와 같다.

    실내 공조는 에어컨의 전원을 켜 희망온도를 설정한다.

    전원이 켜져있는 동안 원하는 값으로 변경할 수 있다.

    에어컨의 전원이 켜져있는 동안 실내온도와 희망온도와 같다면 에어컨이 켜져 있는 동안은 실내 온도가 변하지 않는다.
    다르다면 희망온도와 같아지는 방향으로 1도 상승 또는 하강한다.

    에어컨의 전원을 끄면 실내온도가 실외온도와 같아 지는 방향으로 매 분 1도 상승 또는 하강한다.

    에어컨의 소비전력은 현재 실내온도에 따라 달라진다.

    희망온도와 실내온도가 다르다면 매 분 전력을 a만큼 소비하고 희망온도와 실내 온도가 같다면 매분 전력을 b만큼 소비한다.

    에어컨이 꺼져있다면 전력을 소비하지않는다.

    희망온도에 따라 전력의 소비량이 다르다.

    희망온도를 통해 최적의 전력 소비량을 분석한다.

    희망온도는 t1, t2 사이에 존재한다.

"""
from copy import deepcopy

def get_possible_setting(temperature, t1, t2, onboard):

    times = len(onboard)

    low = temperature - times
    high = temperature + times

    if t1 < low < t2:
        t1 = low

    if t1 < high < t2:
        t2 = high

    return t1, t2

def find_getting_in_time(onboard):
    get_out_status = 0
    getting_in_time = None
    for i in range(len(onboard)):
        if onboard[i] != get_out_status:
            getting_in_time = i
            break
    return getting_in_time

def find_getting_out_time(onboard):

    get_in_status = 1
    getting_out_time = None
    if onboard[-1] == get_in_status:
        return

    for i in range(len(onboard), -1, -1):
        if onboard[i] == get_in_status:
            getting_out_time = i+1
            break

    return getting_out_time

def cal_electricity(temperature, t1, t2, a, b, onboard, desired):
    for i in range(len(onboard)):
        # 탑승

def solution(temperature, t1, t2, a, b, onboard):
    answer = 0


    #최소/최대 온도는 onboard의 길이에 영향을 받는다.
    # ex) onboard => 7 쾌적한 최소 온도가 18도이더라도 현재 설정된 실내온도(실외온도와 동일)가 28도이기 때문에
    # 28 - 7 = 21이다. 최대 온도는 28 + 7 이지만 최적의 실내 최대온도는 26도로 지정되어있기 떄문에 26도 설정된다.
    # 가능한 범위 내에서 희망온도를 찾기위함이다.

    t1, t2 = get_possible_setting(temperature, t1, t2, onboard)

    desired_temp = t1 + t2 // 2

    while t1 < desired_temp < t2:
        # 에너지 소비 계산

    return answer

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


def solution(temperature, t1, t2, a, b, onboard):
    answer = 0

    # 희망 온도
    desired_temp = t1 + t2 // 2

    while t1 < desired_temp < t2:
        for i in range(len(onboard)):

    return answer

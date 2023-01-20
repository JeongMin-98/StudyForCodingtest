"""

    각 자리 수가 0 ~ 9 로만 이루어진 문자열 S

    'X' 혹은 '+' 연산자를 넣어 연산

    연산 순서는 기존의 사칙연산 순서가 아니라 무조건 왼쪽에서부터 순서대로 계산

    1 < S <= 20

"""


def solution(s):
    answer = 1
    temp = None
    for i in s:
        if int(i) == 1 or int(i) == 0:
            temp = int(i)
        else:
            if temp is not None:
                answer *= (temp + int(i))
                temp = None
            else:
                answer *= int(i)

    if temp is not None:
        answer += temp
    return answer


if __name__ == '__main__':
    num = input()
    print(solution(num))

"""

    AC 언어

    R => 뒤집기 순서를 뒤집는 함수
    D => 첫 번쨰 수를 버리는 함수

    deque

    [0, 1, 2, 3]
    default 상황:
    popleft
    R 한번 적용된 상황:
    popright


    배열이 비어있는데 D를 사용하는 경우에는 에러가 발생한다.

    에러가 발생할 경우 무조건 error로 표시한다.

"""
from collections import deque


def ac(cmd, number):
    status = {0: 1, 1: 0}
    r_status = 0
    error = 0
    number = deque(number)
    for f in cmd:
        if f == 'R':
            r_status = status[r_status]
        if f == 'D':
            if not number:
                error = 1
                break
            if r_status:
                number.pop()
            else:
                number.popleft()

    return list(number), r_status, error


def main(cmd, number):
    value, r, e = ac(cmd, number)

    if e:
        print('error')
    else:
        if r:
            value = value[::-1]

        result = ','.join(value)
        result = '[' + result + ']'
        print(result)


def convert(array):
    if not array[1:-1]:
        return []
    return array[1:-1].split(',')


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        cmd = input()
        N = int(input())
        array = convert(input())
        main(cmd, array)

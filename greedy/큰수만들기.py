"""
    숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 한다.

    만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return

    1924

    1924
    1249

    924
    249


    4177252841
    1122445778

    477252841
    122445577

"""


def solution(number, k):
    answer = ''
    for _ in range(k):
        rank = len(number)
        idx = 0
        for i in range(rank):
            if number[i] != number[i+1]:
                idx = i
                break
        if idx == 0:
            idx += 1
        next_number = number[idx:]
        another = number[:idx] + number[idx + 1:]

        number = max(next_number, another)

    answer = number
    return answer


print(solution('4177252841', 4))

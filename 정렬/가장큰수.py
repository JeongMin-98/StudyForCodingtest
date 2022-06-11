from itertools import permutations
from functools import reduce


def solution(numbers):
    answer = ''
    n = len(numbers)
    p = permutations(numbers, n)

    num_p = []


    num_p.append(reduce(lambda x, y: (str(x) + str(y))))

    answer = max(num_p)
    return answer
print(solution([6, 10, 3]))

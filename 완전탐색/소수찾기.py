"""

    numbers 길이 만큼 숫자는 만들어짐

    17 => 71 [::-1]

    i = 1
    1, 7
    i = 2
    17 71

    011
    i = 1
    0, 1, 1,
    i = 2
    01, 11, 10
    i = 3
    011 101 110
"""
import itertools


def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    prime = []
    for i in range(1, len(numbers) + 1):
        ls = list(map(int, map(''.join, itertools.permutations(numbers, i))))
        print(ls)
        for j in range(0, len(ls)):
            if ls[j] <= 1 or ls[j] in prime:
                continue
            if is_prime_number(ls[j]):
                answer += 1
                prime.append(ls[j])
                print(prime)

    return answer
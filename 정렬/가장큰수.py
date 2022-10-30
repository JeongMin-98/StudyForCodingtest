"""

    0 또는 양의 정수가 주어졌을 떄, 정수를 이어 붙여 만들수 있는 가장 큰 수


"""
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*4, reverse=True)
    answer = ('').join(numbers)
    answer = str(int(answer))

    return answer


print(solution([0,0,0,0]))
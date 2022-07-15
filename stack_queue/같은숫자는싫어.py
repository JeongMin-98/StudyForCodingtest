"""

    배열 arr -> 숫자 0 부터 9까지로 이루어짐
    연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    제거된 후 남은 수들을 반환할때, 원소들의 순서를 유지해야함

"""

def solution(arr):
    answer = []

    for i in range(0, len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
            continue
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer

print(solution([4,4,4,3,3]))
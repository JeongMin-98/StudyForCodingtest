"""

    기준 데이터를 설정하고 기준보다 큰데이터와 작은 데이터의 위치를 바꾸는 방식을 사용한다.


"""


def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    rest = arr[1:]

    left = [x for x in rest if x < pivot]
    right = [x for x in rest if x >= pivot]

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right


if __name__ == '__main__':
    # arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(quicksort(arr))

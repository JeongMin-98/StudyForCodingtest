arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(arr):
    """
        처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해
        맨앞에 있는 데이터와 바꾸는 것을 반복
    """
    for i in range(len(arr)):
        min_value = min(arr[i:len(arr)])
        min_value_idx = arr.index(min_value)
        temp = arr[i]
        arr[i] = min_value
        arr[min_value_idx] = temp

    print(arr)


selection_sort(arr)

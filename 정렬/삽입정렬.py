"""

    처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

"""
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break
    return arr


print(insertion_sort(arr))

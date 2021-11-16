def solution(array, commands):
    def merge(arr, left_arr, right_arr):

        l_len = len(left_arr)
        r_len = len(right_arr)

        sl = 0
        sr = 0
        index = 0

        while (sl < l_len) and (sr < r_len):
            if left_arr[sl] < right_arr[sr]:
                arr[index] = left_arr[sl]
                index += 1
                sl += 1
            else:
                arr[index] = right_arr[sr]
                index += 1
                sr += 1
        while sl < l_len:
            arr[index] = (left_arr[sl])
            index += 1
            sl += 1
        while sr < r_len:
            arr[index] = (right_arr[sr])
            index += 1
            sr += 1


    def merge_sort(arr):

        if len(arr) < 2:
            return

        half = len(arr)//2

        left_arr = arr[0:half].copy()
        merge_sort(left_arr)
        right_arr = arr[half:len(arr)].copy()
        merge_sort(right_arr)

        merge(arr, left_arr, right_arr)


    answer = []

    for _command in commands:
        i = _command[0]
        j = _command[1]
        k = _command[2]

        separated_list = array[i-1:j]

        merge_sort(separated_list)

        answer.append(separated_list[k-1])

    return answer


test = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(test, com))

def solution(arr1, arr2):
    answer = []

    size = len(arr1)

    for i in range(0, len(arr1)):
        temp = []
        for j in range(0, len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer


if __name__ == '__main__':
    # arr1 = [[1, 2], [2, 3]]
    # arr2 = [[3, 4], [5, 6]]
    #
    arr1 = [[1], [2]]
    arr2 = [[3], [4]]
    print(solution(arr1, arr2))

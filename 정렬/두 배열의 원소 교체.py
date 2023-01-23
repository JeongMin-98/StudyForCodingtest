"""

    두 개의 배열 A,B를 가지고 있다.
    두 배열은 N개의 원소로 구성되어있고 모두 자연수이다.

    최대 K번의 바꿔치기 연산을 수행 가능

    바꿔치기 연산은 배열 A, B에 있는 각각의 원소를 골라 서로 바꾸는 것을 말한다.

    배열 A의 모든 원소의 합이 최대가 되도록 하는 것

    완료하였을 때 A의 모든 원소의 합의 최댓값은?

"""


def solution(arr1, arr2):
    global N, k
    arr1.sort()
    arr2.sort(reverse=True)

    for i in range(N):
        if k <= 0:
            break
        if arr1[i] < arr2[i]:
            k -= 1
            arr2[i], arr1[i] = arr1[i], arr2[i]
    return sum(arr1)


if __name__ == "__main__":
    N = 5
    k = 3
    A = [1, 2, 5, 4, 3]
    B = [5, 5, 3, 6, 5]

    print(solution(A, B))

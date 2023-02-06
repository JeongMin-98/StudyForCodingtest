"""

    다른 문제: https://www.acmicpc.net/problem/1654

    떡볶이 떡의 길이가 일정하지 않다.

    한 봉지 안에 들어가는 떡의 총 길이는 절단기로 맞춰준다.

    높이 H로 지정하여 떡을 줄지어서 한번에 절단한다.
    낮은 떡은 잘리지 않는다.

    손님이 적어도 M 만큼의 떡을 얻기 위해서 절단기를 설정할 수 있는 높이의 최댓값을 구하라.

"""


def solution(arr, m):
    start = 0
    end = max(arr)
    h = -1

    while start < end:
        cut = 0
        mid = (start + end) // 2

        for x in arr:
            if x > mid:
                cut += (x - mid)

        if cut >= m:
            start = mid + 1
            if cut == m:
                if h <= mid:
                    h = mid
        else:
            end = mid - 1
    return h


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    h = solution(arr, m)
    if h == -1:
        print('정답 X')
    else:
        print(h)

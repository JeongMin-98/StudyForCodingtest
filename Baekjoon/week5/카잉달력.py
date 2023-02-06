"""

    M과 N보다 작거나 같은 두개의 자연수 x,y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현

    1년 <1:1>
    2년 <2:2>

    x < M => x' = x + 1 else x' = 1
    y < N => y' = y+1 else y' = 1

    <M:N> => 마지막 해

    <1:1> => 1 => 1 // 10 1 % 10 => 1, 1 1//12 1%12 => 1, 1

    <1:11> => 11 11:11 11 11//10 11%10 / 11//12 11%12 => 1, 1 / 0, 11
            ==> 1 // 10 1 % 10 => 1, 1 11//12 11%12 => 0, 11
    <2:1> => 12 12:12 2 // 10 2 % 10 => 2, 2 1 // 12 1 % 12 => 1, 1
    (x-1)
    <3:1> => 13 13:13
    <3:9> -> YEAR / 10 => 몫과 나머지
    Year / 12 => 몫과 나머지

    <3:1> => 0, 3 / 0, 1
    year = 몫 * 10 + 나머지
    year = 몫 * 12 + 나머지

    0 60

    10, 12
    9 , 11
    1 => 0, 1, 0, 1 < 1, 1>
    9 => 0, 9, 0, 9 < 9, 9>
    10 => 1, 0, 0, 10 <10, 10>
    11 => 1, 1, 0, 11 <1, 11>
    12 => 1, 2, 1, 0 <2, 1>
    13 => 1, 3, 1, 1 <3, 2>
    14 => 1, 3, 1, 2 <4, 3>
    20 => 2, 0, 1, 8 <1, 8>
    21 =>


    x' > x면 자기보다 큰 year를 뜻함.

    83 => 6, 5,


    3 // 10 3 % 10 2 // 12 2 % 12

    1 3 1 9


"""
import math


def solution(m, n, x, y):
    max_year = m * n // math.gcd(m, n)
    i = 1
    j = 1
    year = -1

    tar_x = i * m + x
    tar_y = j * n + y

    while tar_x < max_year or tar_y < max_year:
        if tar_x > tar_y:
            j += 1
        elif tar_x < tar_y:
            i += 1
        else:
            year = tar_x
            break
        tar_x = i * m + x
        tar_y = j * n + y

    return year


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n, x, y = map(int, input().split())
        print(solution(m, n, x, y))

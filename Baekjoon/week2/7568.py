"""

    문제
    키, 몸무게 => 등수를 매김

    몸무게 num kg 키 y cm이면 (num, y)이다.

    A(num, y), B(p, q)
    num > p, y > q => A
    num < p, y > q => A, B 누가 크지않다.

    자신보다 더 큰 덩치의 사람이 K명이라고 하면, 자신의 랭크는 K+1이다.

"""
N = int(input())
info = []
for i in range(0, N):
    man = list(map(int, input().split()))
    info.append(man)

for a in info:
    rank = 1
    for b in info:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1
    print(rank, end=' ')
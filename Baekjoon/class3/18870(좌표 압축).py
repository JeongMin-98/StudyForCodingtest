"""

    수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

    Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

    X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

    sort

"""
from collections import defaultdict

N = int(input())
coords = list(map(int, input().split()))
compress = list(set(coords))
compress = sorted(compress)
idx_map = defaultdict(int)

for i in range(len(compress)):
    idx_map[compress[i]] = i

for coord in coords:
    print(idx_map[coord], end=' ')
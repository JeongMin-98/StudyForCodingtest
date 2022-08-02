"""

    피로도 시스템 => 0 이상의 정수로 표현

    일정 피로도를 사용해서 던전 탐험 가능

    최소 필요 피로도: 각 던전마다 탐험을 시작하기 위해 필요한 피로도
    소모 피로도: 탐험을 마쳤을 때 소모되는 피로도

"""
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    step = [i for i in range(0, len(dungeons))]
    step = list(map(list, permutations(step, len(step))))
    backup_k = k
    answer = []
    for index in step:
        k = backup_k
        visited = []
        for i in index:
            dungeon = dungeons[i]
            if k >= dungeon[0]:
                k -= dungeon[1]
                visited.append(i)
            # else:
            #     break
        answer.append(len(visited))
    return max(answer)

print(solution(80, [[80, 20],[50,40],[30,10]]))
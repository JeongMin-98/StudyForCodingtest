
def dfs(room, visited, tester_pos, x, y):

    keep_dis = 1

    dest_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited[x][y] = 1
    for dest in dest_list:
        if keep_dis == 0:
            break
        x1 = x + dest[0]
        y1 = y + dest[1]
        in_room = (0 <= x1 < 5) and (0 <= y1 < 5)
        dis = abs(x1 - tester_pos[0]) + abs(y1 - tester_pos[1])
        if in_room and visited[x1][y1] == 0:
            if dis < 3:
                if room[x1][y1] == "P":
                    return 0
                if room[x1][y1] == "O":
                    keep_dis = dfs(room, visited, tester_pos, x1, y1)

        else:
            continue
    return keep_dis


def solution(places):
    answer = []

    ## room travel
    for room in places:
        visited = [[0] * 5 for _ in range(0, 5)]
        keep_dis = []
        for r in range(0, 5):
            for c in range(0, 5):
                if room[r][c] == "P":
                    tester_pos = (r, c)
                    keep_dis.append(dfs(room, visited, tester_pos, r, c))
        if 0 in keep_dis:
            keep_dis = 0
        else:
            keep_dis = 1
        answer.append(keep_dis)

    return answer


# print(solution([["POOOP","OXXOX","OPXPX","OOXOX","POXXP"],["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#                 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

print(solution([['OOOOP',"XXXXX","XXXXX"]]))
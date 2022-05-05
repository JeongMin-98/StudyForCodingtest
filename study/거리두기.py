# dest_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# travel_dest_list = []
# visited = [[0]*5 for _ in range(0, 5)]
#
#
# def near_by_tester(room, i, j, pos):
#     if room[i][j] == 'P':
#         retval = 0
#     elif room[i][j] == 'O':
#         retval = travel_room(room, i, j, pos)
#     elif room[i][j] == 'X':
#         retval = 1
#     else:
#         print("error")
#     return retval
#
# def travel_room(room, i, j, tester_pos):
#     src_r = tester_pos[0]
#     src_c = tester_pos[1]
#     y_n = []
#     for dest in dest_list:
#         r = i + dest[0]
#         c = j + dest[1]
#         length = abs(src_r - r) + abs(src_c - c)
#         if not ((0 <= r < 5) and (0 <= c < 5)):
#             pass
#         else:
#             if length <= 2:
#                 if not (room, r, c, tester_pos) in travel_dest_list and visited[r][c] == 0:
#                     travel_dest_list.append((room, r, c, tester_pos))
#             if len(travel_dest_list) > 0:
#                 travel_pos = travel_dest_list.pop()
#                 visited[travel_pos[1]][travel_pos[2]] = 1
#                 if room[travel_pos[1]][travel_pos[2]] == 'P':
#                     y_n.append(0)
#                 elif room[travel_pos[1]][travel_pos[2]] == 'O':
#                     y_n.append(travel_room(travel_pos[0], travel_pos[1], travel_pos[2], travel_pos[3]))
#                 elif room[travel_pos[1]][travel_pos[2]] == 'X':
#                     y_n.append(1)
#                 else:
#                     pass
#     if 0 in y_n:
#         return 0
#     else:
#         return 1
#
# def find_tester_pos(room):
#     y_n = 0
#     for i in range(0, 5):
#         for j in range(0, 5):
#             if room[i][j] == 'P':
#                 pos = (i, j)
#                 visited[i][j] = 1
#                 y_n = travel_room(room, i, j, pos)
#
#     return y_n
#
# def count_tester(room):
#     tester = 0
#     for row in room:
#         tester = tester + row.count('P')
#     return tester
#
#
# def solution(places):
#     answer = []
#     degree = 0
#     for room in places:
#         if count_tester(room) == 0:
#             degree = 1
#         else:
#             degree = find_tester_pos(room)
#         answer.append(degree)
#     return answer
dest_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[0] * 5 for _ in range(0, 5)]


def near_by_tester(room, i, j, tester_pos):
    keep_dis = 1
    t_r = tester_pos[0]
    t_c = tester_pos[1]

    # check next destination.
    for dest in dest_list:
        i = t_r + dest[0]
        j = t_c + dest[1]
        length = abs(t_r - i) + abs(t_c - j)
        if (0 <= i < 5) and (0 <= j < 5):
            if length <= 2:
                if not(visited[i][j]):
                    visited[i][j] = 1
                    if room[i][j] == 'P':
                        keep_dis = 0
                    elif room[i][j] == 'O':
                        keep_dis = near_by_tester(room, i, j, tester_pos)
                    else:
                        keep_dis = 1
        if not (keep_dis):
            break

    return keep_dis


def solution(places):
    answer = []
    keep_dis = 1
    for room in places:
        visited = [[0] * 5 for _ in range(0, 5)]
        # find tester
        for i in range(0, 5):
            for j in range(0, 5):
                if room[i][j] == 'P':
                    # check tester nearby tester
                    visited[i][j] = 1
                    keep_dis = near_by_tester(room, i, j, (i, j))
                    if not (keep_dis):
                        break
            if not (keep_dis):
                break
        answer.append(keep_dis)

    return answer
print(solution([["POOOP","OXXOX","OPXPX","OOXOX","POXXP"],["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))
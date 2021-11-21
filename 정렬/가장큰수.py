#
# def solution(numbers):
#
#
#     answer = ''
#     def merge_sort(arr):
#
#         if len(arr) < 2:
#             return
#
#         half = len(arr) // 2
#
#         left_arr = arr[0:half]
#         merge_sort(left_arr)
#         right_arr = arr[half:len(arr)]
#         merge_sort(right_arr)
#
#         merge_by_str(arr, left_arr, right_arr)
#
#     def merge_by_str(arr, left_arr, right_arr):
#
#         l_len = len(left_arr)
#         r_len = len(right_arr)
#
#         sl = 0
#         sr = 0
#         index = 0
#
#         while (sl < l_len) and (sr < r_len):
#             DIGIT = bool(len(str(left_arr[sl])) >= len(str(right_arr[sr]))) # 자릿수
#             SIZE = bool(str(left_arr[sl]) > str(right_arr[sr])) # 크기
#             if DIGIT:
#                 if SIZE:
#                     arr[index] = str(left_arr[sl])
#                     sl += 1
#                     index += 1
#                 else:
#                     arr[index] = str(right_arr[sr])
#                     sr += 1
#                     index += 1
#             else:
#
#                 if SIZE:
#                     arr[index] = str(right_arr[sr])
#                     sr += 1
#                     index += 1
#                 else:
#                     arr[index] = str(left_arr[sl])
#                     sl += 1
#                     index += 1
#
#         while sl < l_len:
#             arr[index] = str(left_arr[sl])
#             sl += 1
#             index += 1
#
#         while sr < r_len:
#             arr[index] = str(right_arr[sr])
#             sr += 1
#             index += 1
#
#     merge_sort(numbers)
#
#     answer = ''.join(numbers)
#
#     return answer
#
# print(solution([3, 30, 34, 5, 9]))

# 6 10 2
# => 총 자릿수?
# 6210

# 3 30 34 5 9  = >  1 2 3 4 5
# 총 자릿수 7
# 9534 000  / 9530 000  / 953 0000
# 953430 0 / 95343 00/
# 9534303 / 9534330
# 9534330 => 5433122

def solution(numbers):

    answer = ''

    (i for i in range(numbers))

    # 6 10 2 3 => 1, 2, 3, 4
    # 1432


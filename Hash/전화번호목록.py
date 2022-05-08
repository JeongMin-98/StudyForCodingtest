# from collections import ChainMap
#
#
# def solution(phone_book):
#     answer = True
#
#     phone_book.sort()
#     prefix = ChainMap()
#     prefix_len = 20
#
#     while len(phone_book) > 0:
#         # if not answer:
#         #     break
#         print(prefix.maps)
#         phone_num = dict()
#         number = phone_book.pop(0)
#
#         if len(prefix.keys()) == 0:
#             phone_num[number] = 0
#             prefix = prefix.new_child(phone_num)
#         else:
#             for pre_key in prefix.keys():
#                 pre_yn = number.startswith(pre_key)
#
#                 if pre_yn:
#                     phone_num[pre_key] = number
#                     prefix = prefix.new_child(phone_num)
#                     answer = False
#                     break
#             if not pre_yn:
#                 phone_num[number] = 0
#                 prefix = prefix.new_child(phone_num)
#
#
#     # for phone_num in phone_book:
#     #     # if phone_num not in prefix:
#     #     if len(prefix) == 0:
#     #         prefix[phone_num] = [0]
#     #     else:
#     #         for pre_key in prefix:
#     #             pre_yn = phone_num.startswith(pre_key)
#     #             if pre_yn:
#     #                 prefix[pre_key].append(phone_num)
#     #                 answer = False
#     #         if not pre_yn:
#     #             prefix[phone_num] = [0]
#
#     return answer
#

def solution(phone_book):
    """

    :param phone_book: 전화번호부
    :return: 전화번호부 중 어떤 한 전화번호가 다른 전화번호의 접두사이면 False를 반환 아니면 True를 반환

    처음 단계의 알고리즘 구상:
    dictionary 자료구조를 이용, chainmap 자료구조도 이용
    두 자료구조를 이용하여 hash 알고리즘을 구현하려고 함
    for pre_key in prefix:
        pre_yn = phone_num.startswith(pre_key)
        if pre_yn:
        prefix[pre_key].append(phone_num)
        answer = False

    위와 같이 prefix라는 ChainMap 객체에 접두사에 대한 정보를 다 담고, for을 통해 모든 접두사를 조회하려고 하였다.
    접두사가 포함된 전화번호는 접두사 : 접두사가 포함된 전화번호 식으로 저장할 수 있기 때문에 조회하는 n의 크기가 적을 거라고 예상했다.
    하지만 여러가지의 서로 다른 전화번호가 접두사의 형태로 prefix에 저장된다면 무수히 많은 n개를 조회해야 했다. 그렇기 때문에 다음과 같이
    바꿔 알고리즘을 작성하였다.

    for문을 두번 쓰는 것을 줄이기

    Solution 1.
    전화번호부를 sort해준다. => O(nlogn)
    전화번호의 리스트를 정렬해주면, 앞 부분 전화번호는 바로 뒤 전화번호보다 길이가 짧다.
    그러므로 앞서 나온 전화번호가 뒤에 나오는 전화번호의 접두사인지 바로 판단 가능하다.
    예를 들어 112 1123 24355 33332993 바로 112, 1123를 비교하여 접두사인지 판단가능하다.
    112 1123 223 22343 와 같은 경우 112, 1123의 경우가 접두사가 있는지 없는지 판단하였기에 먼저 앞부분에 발견하면 바로 return False를 시키도록 하였음
    11 12 143 1234 의 경우 11 12 1234 143 으로 정렬되어있기 때문에 탐색에 용이하다.
    """
    phone_book.sort()

    # prefix = ChainMap()
    # prefix_len = 20

    for i in range(1, len(phone_book)):

        # if not answer:
        #     break

        # phone_num = dict()
        number_prefix = phone_book[i - 1]

        # phone_num[number_prefix] = 0
        # prefix = prefix.new_child(phone_num)

        pre_yn = phone_book[i].startswith(number_prefix)
        if pre_yn:
            # phone_num[number_prefix] = phone_book[i]
            # prefix = prefix.new_child(phone_num)
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
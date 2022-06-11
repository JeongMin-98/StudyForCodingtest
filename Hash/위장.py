from itertools import combinations


def solution(clothes):
    answer = 0
    wear = dict()
    for name, types in clothes:
        if types not in wear.keys():
            wear[types] = [name]
        else:
            wear[types].append(name)

    wear_type = list(wear.keys())
    type_n = len(wear.keys())
    if type_n == 1:
        answer += len(wear[wear_type[0]])
        return answer
    if type_n == 30:
        answer = (2 ^ type_n) - 1
        print(answer)
        return answer
    for n in range(1, type_n + 1):
        wear_combs = list(combinations(wear_type, n))
        if n == 1:
            for clothe in wear_combs:
                answer += len(wear[clothe[0]])
        if n >= 2:
            for comb in wear_combs:
                count = 1
                for clothe in comb:
                    count = count * len(wear[clothe])
                answer += count

    return answer



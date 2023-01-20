import itertools


def factorial(n):
    ret = [1, 2]
    if n == 1:
        return ret[0]
    if n == 2:
        return ret[1]
    for i in range(3, n + 1):
        ret.append(i * ret[-1])

    return ret[n - 1]


def solution(n, k):
    lineups = []

    tmp = list(range(1, n + 1))

    # 만들어질수 있는 r번째 원소마다 만들어질 수 있는 경우의 수 n-1!
    r_cnt = factorial(n - 1)
    # k번째 원소가 궁금하다면, k % (n-1)! =>
    # ex) k=5 5 % 2 = 1
    # 5 // 2 = 2
    # r = 2이고 1번째 조합 ()
    r_idx = k % n
    comb_idx = k % r_cnt

    lineup = [tmp[r_idx]]

    tmp.pop(r_idx)

    idx_list = list(itertools.permutations(tmp))
    for idx in idx_list[comb_idx - 1]:
        lineup.append(tmp[idx-1])

    answer = lineup
    return answer

if __name__ == '__main__':

    print(solution(3, 5))
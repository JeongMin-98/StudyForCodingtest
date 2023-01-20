"""

    N 과 K가 공백을 기준으로 하여 각각 자연수로 주어진다.

    N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력

    1) N에서 1을 뺍니다.
    2) N을 K로 나눈다.
    2)번은 N % K == 0일때만 시행 가능




"""


def solution(N, k):
    num = N
    dp = [0] * (N + 1)
    # 1~N 까지 하는 경우 시간 복잡도 O(N) 공간 복잡도 O(N)
    for_cnt = 0
    for i in range(2, N + 1):
        for_cnt += 1
        dp[i] = dp[i - 1] + 1

        if i % k == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // k] + 1)

    while_cnt = 0
    dp = [0] * (N + 1)
    """ 시간 복잡도는 위 코드에 비해 크게 줄지만, 공간 복잡도는 O(N) 이다. """
    while N > 1:
        while_cnt += 1
        if N % k == 0:
            dp[N // k] = dp[N] + 1
            N //= k
        else:
            dp[N - 1] = dp[N] + 1
            N -= 1

    print(f'for_loop : {for_cnt} \n while_loop : {while_cnt}')

    cnt = 0
    last_cnt = 0

    while 1:

        last_cnt += 1
        target = (num // k) * k
        cnt += (num - target)
        num = target

        if num < k:
            break

        num //= k
        cnt += 1

    cnt += (num - 1)

    print(f"last_cnt: {last_cnt}")
    return cnt


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))

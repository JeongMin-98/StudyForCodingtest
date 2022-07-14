"""

    prices : 초 단위로 기록된 주식가격이 담긴 배열

    가격이 떨어지지 않은 기간은 몇초인가 return

    # Divide and Conquer (분할 정복)

    [ 2, 3, 2, 3]
    이후에 1보다 작은 값이 있는 지 확인
    [2,3] =>  둘 중 작은 값  [0:2]
    [2,3] => [2: 4]
"""


def split(next_prices, start, end, key):
    mid = (end-start) // 2
    n = end - start + 1
    if len(next_prices) == 0:
        return None
    if len(next_prices) == 1:
        if key > next_prices[-1]:
            return 0
        else:
            return None
    if n > 2:
        print('split!')
        left_down_index = split(next_prices, start, mid, key)
        right_down_index = split(next_prices, mid+1, start, key)

    else:
        print(next_prices[start], next_prices[end])
        if key > next_prices[start]:
            return start
        if key > next_prices[end]:
            return end
        return None

    if left_down_index is None and right_down_index is None:
        return None
    if left_down_index is None and right_down_index is not None:
        return right_down_index
    if left_down_index is not None and right_down_index is None:
        return left_down_index
    if left_down_index is not None and right_down_index is not None:
        return left_down_index

def solution(prices):

    answer = []

    for i in range(0, len(prices)):
        next_prices = prices[i+1:]
        first_down_index = split(next_prices, 0, len(next_prices)-1, prices[i])
        if first_down_index is None:
            time = len(prices) - i - 1
        else:
            time = first_down_index + 1

        answer.append(time)
        print(answer)
    return answer

print(solution([1,2,3,2,3]))
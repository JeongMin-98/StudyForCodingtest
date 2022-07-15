"""

    prices : 초 단위로 기록된 주식가격이 담긴 배열

    가격이 떨어지지 않은 기간은 몇초인가 return

"""



def solution(prices):

    answer = []

    for i in range(0, len(prices)):
        time = len(prices) - i - 1
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                time = j-i
                break
        answer.append(time)

    answer.append(0)
    return answer

print(solution([3,4,2,3,3]))
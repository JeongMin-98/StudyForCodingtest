"""

    prices : 초 단위로 기록된 주식가격이 담긴 배열

    가격이 떨어지지 않은 기간은 몇초인가 return

    감소하지 않으면 next_price를 increase에 append해주고
    감소하는 순간 중지한다.
"""



def solution(prices):

    answer = []
    increase = []
    past = []
    n = len(prices)
    current = None
    while len(past) < n:
        if current is None:
            current = prices.pop(0)
        if len(prices) > 0:
            if current <= prices[0]:
                increase.append(prices.pop(0))
            else:
                past.append(current)
                current = None
                if len(increase) == 0:
                    answer.append(1)
                else:
                    answer.append(len(increase)+1)
                    prices = increase + prices
                    increase = []
        else:
            answer.append(len(increase))
            prices = increase
            past.append(current)
            current = None
            increase = []
        print("past {}, current {}, prices {},  increase {} ".format(past, current, prices, increase))

    return answer

print(solution([3,4,2,3,3]))
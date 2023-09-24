"""

    이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다.

     우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다.

     데이터를 삽입하는 연산

     데이터를 삭제하는 연산
      우선순위가 가장 높은 것을 삭제하기 위한 것이고
      다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것

"""
import heapq

queue = []


def calculation(cal, num):
    if cal == 'I':
        heapq.heappush(queue, num)
    elif cal == 'D':
        if num == -1:
            try:
                heapq.heappop(queue)
            except IndexError:
                pass
        elif num == 1:
            try:
                queue.pop()
            except IndexError:
                pass

T = int(input())
for _ in range(T):
    count = int(input())
    queue = []
    for i in range(count):
        cal, num = input().split()
        calculation(cal, int(num))
    if queue:
        print("{} {}".format(queue[-1], queue[0]))
    else:
        print("EMPTY")
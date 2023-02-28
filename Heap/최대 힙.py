"""

    [Baekjoon] https://www.acmicpc.net/problem/11279

    최대 힙

    부모노드의 키값이 자식 노드이 키값보다 항상 큰 힙



"""
import heapq
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    h = []
    for _ in range(N):
        x = int(sys.stdin.readline())

        if x == 0:
            if not h:
                print(0)
            else:
                value = heapq.heappop(h)
                print(value * (-1))
        else:
            heapq.heappush(h, -1 * x)

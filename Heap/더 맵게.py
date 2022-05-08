import heapq


def solution(scoville, K):
    answer = 0

    heap = []
    mix = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return answer
    else:
        while 1:

            min_s = heapq.heappop(scoville)
            if min_s >= K:
                break
            if len(scoville) == 0:
                break
            new_food = min_s + heapq.heappop(scoville)*2
            heapq.heappush(scoville, new_food)
            mix += 1

            new_food = 0

        if min_s < K:
            return -1
        else:
            answer = mix
    return answer


print(solution([1,2,3,9,10,12], 7))
def makegrid(count):
    grid = []
    if count == 1:
        grid = [[1, 1]]
        return grid
    for i in range(1, count):
        if count % i == 0:
            if (count // i) >= i:
                grid.append([count // i, i])
    return grid


def solution(brown, yellow):
    answer = []

    mul = makegrid(yellow)

    for yellow_size in mul:
        count = (yellow_size[0] * 2) + (yellow_size[1] * 2) + 4
        if brown == count:
            return [yellow_size[0] + 2, yellow_size[1] + 2]

    return answer

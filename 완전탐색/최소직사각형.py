"""

    완전탐색



"""
def find_size(i, j, sizes, maxsize):
    if i == len(sizes):
        return sizes[i-1][0] * sizes[j][1]
    elif j == len(sizes):
        return sizes[i][0] * sizes[j-1][1]
    elif i == len(sizes) and j == len(sizes):
        return sizes[i-1][0] * sizes[j-1][1]

    w = sizes[i][0]
    h = sizes[j][1]

    area = w * h
    if area > maxsize:
        return area
    else:
        a = find_size(i+1, j, sizes, maxsize)
        b = find_size(i, j+1, sizes, maxsize)
        if a > b:
            return b
        else:
            return a

def solution(sizes):
    answer = 0

    area = [w * h for w, h in sizes]
    maxsize = max(area)

    answer = find_size(0, 0, sizes, maxsize)

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
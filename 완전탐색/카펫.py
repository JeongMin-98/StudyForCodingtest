"""

 b b b b
 b y y b
 b b b b

    카펫의 가로 길이 >= 세로 길이
  b b b
  b y b
  b b b

  6 * 4
  12 + 8 + 4 = 24
  b b b b b b b b
  b y y y y y y b
  b y y y y y y b
  b y y y y y y b
  b y y y y y y b
  b b b b b b b b

  2 * 1
  3 * 1
  6 + 2 + 4 = 12
  4 * 1
  8 + 2 + 4 = 14
  2 * 2
   b b
 b y y b
 b y y b
   b b
   2 * 2
   2 * 2 + 2 * 2 + 4

   yellow 의 개수는
   4 => 1,2,4
   6 => 1,2,3,6

   yellow 가로 길이는 세로 길이보다 같거나 크다.
   4 => [2,2], [4,1]
   ======> 12, 14
   mul = []
   for i in range(1, yellow):
       if yellow % i == 0:
           mul.append(yellow//i, i)
"""
def makegrid(count):
    grid = []
    if count == 1:
        grid = [[1,1]]
        return grid
    for i in range(1, count):
        if count % i == 0:
            if(count // i) >= i:
                grid.append([count // i, i])
    return grid

def solution(brown, yellow):
    answer = []

    mul = makegrid(yellow)

    for yellow_size in mul:
        count = (yellow_size[0] * 2) + (yellow_size[1] * 2) + 4
        if brown == count:
            return [yellow_size[0]+2,yellow_size[1]+2]

    return answer

print(solution(10, 2))
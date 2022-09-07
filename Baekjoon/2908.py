"""

    상근이는 세 자리 수 두개를 쓴다.

    그 중 큰 수를 말해보라고 함.

    상수는 수를 다른 사람과 다르게 거꾸로 읽는다.

    예제
    734 893

    출력

    437 398

    437

    풀이:
    0이 포함 되지 않은 수
    340 => 043 => 43 이런 경우는 X
    입력 값을 먼저 str상태에서 reversed 해준다.
    그리고 int값으로 변환 후 크기 비교
    그런 다음 큰 수를 출력
"""

num = input().split()

num = list(map(int ,map(lambda x:x[::-1], num)))

if num[0] > num[1]:
    print(num[0])
else:
    print(num[1])
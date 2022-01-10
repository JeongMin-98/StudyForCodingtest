def solution(participant, completion):
    p_dict = dict()

    # completion for문 -> 참가 여부 정함.
    for player in participant:
        if player in p_dict:
            p_dict[player].append(0)
        else:
            p_dict[player] = [0]

    for player in completion:
        if player in p_dict:
            p_dict[player].pop(0)

    for p_com_yn in p_dict:
        if len(p_dict[p_com_yn]) != 0:
            answer = p_com_yn

    return answer

participant = ['one', 'two', 'one', 'three']

completion = ['one', 'two', 'three']

print(solution(participant, completion))
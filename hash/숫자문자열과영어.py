number_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3' , 'four':'4',
               'five':'5', 'six':'6', 'seven':'7', 'eight':'8',
               'nine':'9'
               }


def phase_s(s):

    for i in range(0, len(s)+1):
        phased_s = s[0:i]

        if '0' <= phased_s <= "9":
            return phased_s, i

        if len(phased_s) >= 3:
            ret_num = find_value(phased_s)
            if ret_num:
                return ret_num, i


def find_value(phased_s):

    if phased_s in number_dict.keys():
        ret_num = number_dict[phased_s]
        return ret_num
    return None


def solution(s):
    answer = ''

    while len(s) > 0:
        change_num, popedNum = phase_s(s)
        answer = answer + change_num
        s = s[popedNum:]

    answer = int(answer)

    return answer


print(solution("2three45sixseven"))
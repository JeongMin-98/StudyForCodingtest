"""

    "()()" , "(())" 올바른 괄호
    "())()", "(()))" 올바르지않은 괄호
    stack -> open_bracket = [] 열린 괄호를 담고

    닫힌 괄호를 만날 때 마다 stack의 top에서 pop한다.

"""

def solution(s):
    answer = True

    # 여는 괄호를 담는 stack
    open_bracket = []
    for i in s:
        if i == '(':
            open_bracket.append(i)
        else:
            if len(open_bracket) == 0:
                return False
            else:
                open_bracket.pop(-1)
    if len(open_bracket) > 0:
        return False
    return answer
    # while len(s[i:]) > 0:
    #     cur = s[i]
    #     i += 1
    #     if cur == '(':
    #         open_bracket.append(cur)
    #     else:
    #         if len(open_bracket) == 0:
    #             return False
    #         else:
    #             open_bracket.pop(-1)
    # if open_bracket == []:
    #     return True


test_case = ['()()', '(())()', ')()(', "(()("]

for s in test_case:
    print(solution(s))


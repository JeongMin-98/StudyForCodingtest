def solution(numbers, target):

    answer = 0

    def change_num(level, numbers, negative):

        temp_list = numbers.copy()
        if negative == 1:
            temp_list[level] = -temp_list[level]

        changed_num = temp_list

        return changed_num

    def dfs(level, numbers, target):
        nonlocal answer

        # 각각의 레벨의 해당하는 숫자를 바꿔준다.

        if level < len(numbers):
            if sum(numbers) == target:
                answer = answer + 1
            else:
                next_num = change_num(level, numbers, 1)
                dfs(level+1, next_num, target)
                dfs(level+1, numbers, target)
        else:
            if sum(numbers) == target:
                answer = answer+1
            else:
                return 1

    dfs(0, numbers, target)

    return answer

if __name__ == "__main__":

    nums = [1, 1, 1, 1, 1]
    t = 3
    print(solution(nums, t))


""" 트리 형식은 너무 오래 걸림
num_list에 하나하나 담아서 할 경우 너무 많은 반복이 일어나고, Target_num보다 큰 수만 자식을 만들어 줘도 시간이 오래 걸릴 수 있다.
def solution(numbers, target):

    def make_list(parents, target_num):

        if sum(parents) > target_num:
            for i in range(len(numbers)):
                parent = parents.copy()
                parent[i] = -parent[i]
                if (parent not in num_list) & (parent not in checked_list) & (sum(parent) >= target_num):
                    # if parent not in num_list:
                    child = parent.copy()
                    num_list.append(child)

        return 0

    answer = 0
    target_list = []
    num_list = []
    checked_list = []

    num_list.append(numbers)


    while len(num_list) != 0:

        check = num_list.pop(0)
        checked_list.append(check)
        if sum(check) == target:
            target_list.append(check)
            answer = answer + 1
        else:

            pass

        make_list(check, target)

    answer = len(target_list)

    return answer


if __name__ == "__main__":

    nums = [1, 1, 1, 1, 1]
    t = 3
    print(solution(nums, t))

"""

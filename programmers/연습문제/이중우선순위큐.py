def solution(operations):
    answer = []

    max_queue = []
    min_queue = []
    queue = []

    for operation in operations:
        oper = operation.split(' ')[0]
        num = int(operation.split(' ')[1])

        if oper == 'I':
            queue.append(num)
            if min_queue:
                min_queue[-1] = min(min_queue[-1], num)
            else:
                min_queue.append(num)
            if max_queue:
                max_queue[-1] = max(max_queue[-1], num)
            else:
                max_queue.append(num)

        if oper == 'D':
            if not queue:
                continue
            if num == 1:
                queue.pop(queue.index(max_queue[-1]))
                if queue:
                    max_queue[-1] = max(queue)
            elif num == -1:
                queue.pop(queue.index(min_queue[-1]))
                if queue:
                    min_queue[-1] = min(queue)

            if not queue:
                max_queue = []
                min_queue = []

    if not queue:
        return [0, 0]
    else:
        return [max_queue[-1], min_queue[-1]]


if __name__ == '__main__':
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))

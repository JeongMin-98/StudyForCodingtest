import random

# n: number

rotate = 0
random_list = []
random_list_length = 10000


def make_random_list(arr):
    for i in range(random_list_length):
        arr.append(random.randint(0, 100000))
    return arr


def get_rotate_count(arr):
    rotate_count = 0
    standard = 1000
    n_count = int(1e9)

    while n_count > 100:
        n_count = 0

        for i in range(len(arr)):
            if arr[i] > standard:
                n_count += 1
        standard += 1000
        rotate_count += 1
    return rotate_count


rotate = get_rotate_count(make_random_list(random_list))
print(rotate)

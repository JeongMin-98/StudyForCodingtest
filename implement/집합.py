"""

    [Baekjoon] https://www.acmicpc.net/problem/11723

    이미 python에는 set이 있지만 구현해봄

    비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다

"""
import sys


class SpecialSet:

    def __init__(self):
        self.isin = [0] * 21

    def check(self, x):
        if self.isin[x]:
            return 1
        else:
            return 0

    def add(self, x):
        if not self.check(x):
            self.isin[x] = 1
        else:
            pass

    def remove(self, x):
        if self.check(x):
            self.isin[x] = 0

    def toggle(self, x):
        if self.check(x):
            self.isin[x] = 0
        else:
            self.isin[x] = 1

    def all(self):
        self.isin = [1] * 21

    def empty(self):
        self.isin = [0] * 21


def parser(cmd, obj=SpecialSet):
    cmd = cmd.split()
    if len(cmd) > 1:
        value = int(cmd[1])
        cmd = cmd[0]
    else:
        cmd = cmd[0]
        value = None

    if cmd == 'add':
        obj.add(value)
        return

    if cmd == 'check':
        print(obj.check(value))
        return

    if cmd == 'remove':
        obj.remove(value)
        return

    if cmd == 'toggle':
        obj.toggle(value)
        return

    if cmd == 'all':
        if value is None:
            obj.all()
        return

    if cmd == 'empty':
        if value is None:
            obj.empty()
        return


if __name__ == '__main__':
    M = int(input())
    a = SpecialSet()
    for _ in range(M):
        cmd = sys.stdin.readline()
        parser(cmd, a)

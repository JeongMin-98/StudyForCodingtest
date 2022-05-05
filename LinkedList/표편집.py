"""
    structure ->
    doubly linked list

    Top, data, Bot

    head <=> last


    method:
    U X -> 현재 위치에서 부터 2개 위
    D X -> 현재 위치에서 부터 X개 아래
    C -> 현재 위치에서 삭제
    Z -> 마지막에 지웠던 위치 기억후 복원, 삭제된 노드가 없을 경우 복원 X


"""


class Node:
    def __init__(self, data):
        self.top = None
        self.data = data
        self.bot = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.temp = None
        self.memory = []

    def add(self, name):
        # 마지막 부분에 무조건 붙음
        addNode = Node(name)
        if self.head is None:
            self.head = addNode
            self.last = addNode
        else:
            self.last.bot = addNode
            addNode.top = self.last
            self.last = addNode

    def set_temp(self, k):
        self.temp = self.head
        for _ in range(0, k):
            # k번째 node로 순회
            self.temp = self.temp.bot

    def upper_x(self, x):
        for _ in range(0, x):
            self.temp = self.temp.top
        return 1

    def down_x(self, x):
        for _ in range(0, x):
            self.temp = self.temp.bot
        return 1

    def cut(self):
        cutNode = self.temp
        if self.temp.bot is None:
            self.temp = self.temp.top
        else:
            self.temp = self.temp.bot
        if cutNode.bot is None:
            topNode = cutNode.top
            topNode.bot = None
            self.last = topNode
            self.memory.append(cutNode)



        if cutNode.top is None:
            botNode = cutNode.bot
            self.head = botNode
            self.memory.append(cutNode)


        if cutNode.bot and cutNode.top:
            topNode = cutNode.top
            botNode = cutNode.bot
            topNode.bot = botNode
            botNode.top = topNode
            self.memory.append(cutNode)
        del cutNode


    def recovery(self):
        recNode = self.memory.pop()
        top_recNode = recNode.top
        bot_recNode = recNode.bot

        if top_recNode is None:
            recNode.bot = self.head
            self.head.top = recNode
            self.head = recNode
        if bot_recNode is None:
            self.last.bot = recNode
            recNode.top = self.last
            self.last = recNode

        if top_recNode and bot_recNode:
            top_recNode.bot = recNode
            bot_recNode.top = recNode
        return 1

    def cli(self, cmd):
        # command line interface
        # U X => Up doublelinkedlist travel
        if cmd[0] == "D":
            return self.down_x(int(cmd[2:]))

        if cmd[0] == "U":
            return self.upper_x(int(cmd[2:]))
        if cmd[0] == "C":
            return self.cut()
        if cmd[0] == "Z":
            return self.recovery()
    def check_diff(self, answer):
        while len(self.memory) > 0:
            delete_node = self.memory.pop()
            answer[delete_node.data] = 'X'
        return answer
def solution(n, k, cmd):
    answer = ''

    shell = DoubleLinkedList()

    for i in range(0, n):
        shell.add(i)

    shell.set_temp(k)

    for line in cmd:
        shell.cli(line)

    answer = ['O'] * n
    answer = shell.check_diff(answer)
    answer = "".join(answer)

    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
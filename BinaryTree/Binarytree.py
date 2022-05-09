"""

    트리는 각 노드들이 서로 엣지로 연결되어 있는 비선형 구조이다.
    트리에는 사이클이 존재할 수 없다.

    + 루트 노드(root): 트리에서 최상위 노드
    + 말단 노드(leaf): 자식이 없는 노드, 말단 노드
    + 노드의 크기: 자신을 포함한 모든 자손 노드의 개수
    + 노드의 깊이(노드의 레벨): 루트에서 해당 노드에 도달하기 위해 거쳐야하는 간선의 수
    + 노드의 높이: 리프에서 해당 노드까지 도달하기 위해 거쳐야하는 간선의 수.
    + 노드의 차수: 하위 트리 개수
    + 트리의 레벨(height): 루트 노드의 height
    + 각 노드는 부모노드나 자식 노드를 가질 수 있다.
    + 각 노드는 어떤 자료형으로도 표현 가능하다.

    이진트리 -> 이진 트리의 노드들이 최대 2개의 자식 노드를 가질 수 있다.


"""


class Node:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):

        if self.root is None:
            self.root = Node(data)
            return
        else:
            current = self.root
            self.search_tree(current, data)

    def search_tree(self, current, data):

        if current.data < data:
            if current.right is None:
                current.right = Node(data)
                return
            else:
                self.search_tree(current.right, data)
        else:
            if current.left is None:
                current.left = Node(data)
            else:
                self.search_tree(current.left, data)

    def print_tree(self, node=None):
        """
        해당 노드로 부터 자식 노드 들을 출력
        :param node:
        :return:
        """
        if node is None:
            current_node = self.root
            print("root node")
        else:
            current_node = node
        print(current_node.data)

        if current_node.left is not None:
            print("{}'s child left node".format(current_node.data))
            self.print_tree(current_node.left)

        if current_node.right is not None:
            print("{}'s child right node".format(current_node.data))
            self.print_tree(current_node.right)

    def remove(self, data):
        """
        data를 가진 노드를 처음 발견 할 시 삭제 한다.
        1. 자식이 하나인경우
        2. 자식이 둘인 경우
        3. 자식이 없는 (단말 노드인 경우)
        :param data:
        :return: (remove node)
        """




bt = BinaryTree()

# lst = [3, 6, 12, 14]
# for i in range(0, len(lst)):
#     root.add(lst[i])
bt.add(9);
bt.add(4);
bt.add(17);
bt.add(3);
bt.add(6);
bt.add(22);
bt.add(5);
bt.add(7);
bt.add(20);
bt.print_tree()

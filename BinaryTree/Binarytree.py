"""

    트리는 각 노드들이 서로 엣지로 연결되어 있는 비선형 구조이다.
    트리에는 사이클이 존재할 수 없다.


    + 루트 노드(root): 트리에서 최상위 노드
    + 말단 노드(leaf): 자식이 없는 노드, 말단 노드
    + 부모 노드: 적어도 하나의 자식 노드를 가지고 있는 노드
    + 자식 노드: 부모 노드의 하위 노드
    + 노드의 깊이(노드의 레벨): 루트에서 해당 노드에 도달하기 위해 거쳐야하는 간선의 수
    + 노드의 높이: 리프에서 해당 노드까지 도달하기 위해 거쳐야하는 간선의 수.
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


    def print_tree_traversal(self, node=None, mode='inorder'):

        if node is None:
            current = self.root
        else:
            current = node
        if mode == 'inorder':
            print("print Inorder Traversal")
            self.inorder(current)
        if mode == 'postorder':
            print("print Postorder Traversal")
            self.postorder(current)
        if mode == 'preorder':
            print("print Preorder Traversal")
            self.preorder(current)

    def inorder(self, node):

        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
        else:
            return

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
        else:
            return

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
        else:
            return


    def print_tree(self, node=None):
        """
        root로부터 전체 트리 출력
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

        if self.root is None:
            print('empty Tree')
            return

        success_remove_yn = self.search_remove_node(None, self.root, data)

        return success_remove_yn

    def search_remove_node(self, parent=None, current=None, data=None):

        if data < current.data:
            return self.search_remove_node(current, current.left, data)
        elif data > current.data:
            return self.search_remove_node(current, current.right, data)
        elif data == current.data:
            # Only one child
            if parent is None and current == self.root:
                min_node = self.find_min_node_data()
                right = self.root.right
                self.root = min_node
                self.root.right = right
                return 1
            else:
                if data < parent.data:
                    if current.left is None:
                        parent.left = current.right
                        del current
                        return True
                    elif current.right is None:
                        parent.left = current.left
                        del current
                        return True
                elif data > parent.data:
                    if current.left is None:
                        parent.right = current.right
                        del current
                        return True
                    elif current.right is None:
                        parent.right = current.left
                        del current
                        return True
            min_node = self.find_min_node_data(current)
            right = current.right
            current = min_node
            current.right = right
            del current
            return True

        else:
            return False

    def find_min_node_data(self, node=None):

        if node is None:
            node = self.root

        if self.root is None:
            print('empty tree')

        current = node
        while current.left is not None:
            current = current.left

        return current

bt = BinaryTree()

# lst = [3, 6, 12, 14]
# for i in range(0, len(lst)):
#     root.add(lst[i])
bt.add(50)
bt.add(30)
bt.add(70)
bt.add(20)
bt.add(40)
bt.add(60)
bt.add(80)
bt.remove(20)
bt.remove(30)
bt.print_tree_traversal(mode = "inorder")
bt.remove(70)
bt.print_tree_traversal(mode = "inorder")

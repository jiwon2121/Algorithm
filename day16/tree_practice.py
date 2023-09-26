import sys
sys.stdin = open('input1.txt')

class Tree:
    def __init__(self):
        self.nodes = []
        self.length = 0

    def add_node(self, node):
        self.nodes.append(node)
        self.length += 1

    def search(self, start = None):
        if start == None:
            start = self.nodes[0]
        result = []
        result.append(str(start.num))

        if start.left != None:
            result.extend(self.search(start = start.left))

        if start.right != None:
            result.extend(self.search(start = start.right))

        return result

    def __str__(self):
        return ' '.join(self.search())


class Node:
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.left = None
        self.right = None

    def add_child(self, child):
        if self.left == None:
            self.left = child

        else:
            if child.num < self.left.num:
                self.left, self.right = child, self.left

            else:
                self.right = child

    def add_parent(self, parent):
        self.parent = parent



V = int(input())

array = list(map(int, input().split()))
my_tree = Tree()

for i in range(1, V+1):
    my_tree.add_node(Node(i))

for i in range(0, len(array), 2):
    p = array[i]
    c = array[i + 1]
    my_tree.nodes[p-1].add_child(my_tree.nodes[c-1])
    my_tree.nodes[c-1].add_parent(my_tree.nodes[p-1])

print(my_tree)

class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def __str__(self):
        result = str(self.value) + ': ['
        for n in self.nodes:
            result += str(n.value) + ' '
        result += ']'
        return result

    def __repr__(self):
        return str(self.value)


node1 = Node(1)
node2 = Node(2)
node7 = Node(3)
node8 = Node(8)

node2.nodes.append(node7)
node2.nodes.append(node8)

node3 = Node(3)

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node9 = Node(8)
node10 = Node(9)
node4.nodes.append(node9)
node9.nodes.append(node10)

node1.nodes.append(node2)
node1.nodes.append(node3)
node3.nodes.append(node4)
node4.nodes.append(node5)
node4.nodes.append(node6)


def find(node):
    if not node.nodes:
        return 1, node
    max = 1
    for n in node.nodes:
        result, last = find(n)
        if last in node.nodes and abs(n.value - node.value) == 1:
            max = result + 1
        else:
            pass


def path(node, target):
    path = []
    _, path = depthSearch(node,target,path)
    return path



def depthSearch(node, target, path):

    if node == target:
        path.append(node)
        return True, path
    else:
        for n in node.nodes:
            result = depthSearch(n, target, path)
            if result:
                path.append(node)
                return True, path
    return False, []

print(path(node3, node10))




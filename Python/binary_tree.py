class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node1 = Node(6)
node2 = Node(8)
node1.left = node2
node3 = Node(5)
node1.right = node3

node4 = Node(1)
node3.right = node4
node5 = Node(7)
node3.left = node5

node6 = Node(9)
node2.right = node6
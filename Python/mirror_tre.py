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

def print_tree(node):
    print(node.value)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)



def mirror(node):
    if node.left or node.right:
        (node.left, node.right) = (node.right, node.left)
        if node.left:
            mirror(node.left)
        if node.right:
            mirror(node.right)

print_tree(node1)
print('Zamiana')
mirror(node1)
print_tree(node1)
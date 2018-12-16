class Node:
    def __init__(self, value):
        #powinno tu byc id, ale mi sie nie chce, więc zakładam, że value jest unikalne
        self.right = None
        self.left = None
        self.value = value

node1 = Node(5)
node2 = Node(2)
node3 = Node(3)
node4 = Node(1)
node5 = Node(6)
node6 = Node(9)
node7 = Node(0)

node1.right = node2
node1.left = node3
node2.right = node4
node2.left = node5
node3.right = node6
node5.left = node7

def add(node,list):
    if node.right != None:
        list.append(add(node.right,list))
    if node.left != None:
        list.append(add(node.left,list))
    else:
        return node.value
    return node.value

# def toList(node):
#     list = []
#     add(node,list)
#     list.append(node.value)
#     return list
#
# print(toList(node1))

def toList(node):
    if node == None:
        return [None]
    return [node.value,toList(node.left),toList(node.right)]

list = toList(node1)
# print(list)

def fromList(list):
    if list == [None]:
        return None
    node = Node(list[0])
    node.left = fromList(list[1])
    node.right = fromList(list[2])
    return node

# print(toList(fromList(list)))


def breodthFirstSearch(node,end):
    q = []
    q.append(node)
    i = 0
    while q != []:
        if q[i] == end:
            return True
        else:
            if q[i].left != None:
                q.append(q[i].left)
            if q[i].right != None:
                q.append(q[i].right)
            q.pop(i)
    return False

m = []

def depthSearch(node,target,memo):
    if node == target:
        memo.append(node.value)
        return True, memo[:]
    else:
        if node.left:
            to_return, memo = depthSearch(node.left,target,memo)
            if to_return:
                memo.append(node.value)
                return True, memo[:]
        if node.right:
            to_return, memo = depthSearch(node.right,target,memo)
            if to_return:
                memo.append(node.value)
                return True, memo[:]
    return False, memo


def lowestCommonAncestor(root, a, b):
    moves_a = []
    moves_b = []
    _, moves_a = depthSearch(root,a, moves_a)
    _, moves_b = depthSearch(root,b, moves_b)
    dif = abs(len(moves_a) - len(moves_b))
    return moves_a[-(dif+1)]

print(lowestCommonAncestor(node1, node7, node4))


def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.value)
    if node.right:
        in_order(node.right)

def pre_order(node):
    print(node.value)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)



pre_order(node1)








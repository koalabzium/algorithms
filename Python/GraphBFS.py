class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def __str__(self):
        result = str(self.value) + ': ['
        for n in self.nodes:
            result += str(n.value) + ','
        result += ']'
        return result


class Graph:
    def __init__(self, l):
        self.list = l


l = [[1, 2], [2, 3], [2, 4], [2, 5], [3, 5], [6, 7]]


def bfs(node, target):
    q = []
    visited = set()
    q.append(node)
    for node in node.nodes:
        q.append(node)
    while q:
        tmp = q[0]
        if tmp == target:
            return True
        else:
            visited.add(q[0].value)
            q.pop(0)
            for node in tmp.nodes:
                if node.value not in visited:
                    q.append(node)
    return False


def dfs_helper(node, target, visited):
    visited.add(node.value)
    if node == target:
        print(visited)
        return True
    if not node.nodes:
        return False
    for n in node.nodes:
        if n.value not in visited:
            result = dfs_helper(n, target, visited)
            if result:
                return True
    print(visited)
    return False


def dfs(node, target):
    visited = set()
    return dfs_helper(node, target, visited)


def fromList(list):
    nodes = {}
    for e in list:
        if e[0] not in nodes:
            node1 = Node(e[0])
            nodes[e[0]] = node1
        else:
            node1 = nodes[e[0]]
        if e[1] not in nodes:
            node2 = Node(e[1])
            nodes[e[1]] = node2
        else:
            node2 = nodes[e[1]]
        node1.nodes.append(node2)
        node2.nodes.append(node1)
    result = []
    for key in nodes:
        result.append(nodes[key])
    return result


nodes = fromList(l)

# for i in nodes:
#     print(i)

print(bfs(nodes[5], nodes[6]))

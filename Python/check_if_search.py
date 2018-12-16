import binary_tree as bt

def check_if_search(node):
    left_res = True
    right_res = True
    if node.left != None:
        if node.left.value < node.value:
            return False
        left_res = check_if_search(node.left)
    if node.right != None:
        if node.right.value > node.value:
            return False
        right_res = check_if_search(node.right)
    if not (left_res and right_res):
        return False
    return True


print(check_if_search(bt.node1))
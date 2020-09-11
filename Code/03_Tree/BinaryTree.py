# coding:utf-8

class Node(object):
    """定义节点"""

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""

    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """加入节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("breadth travel:")
    tree.breadth_travel()  # 0 1 2 3 4 5 6 7 8 9
    print()
    print("preorder:")
    tree.preorder(tree.root)  # 0 1 3 7 8 4 9 2 5 6
    print()
    print("inorder:")
    tree.inorder(tree.root)  # 7 3 8 1 9 4 0 5 2 6
    print()
    print("postorder:")
    tree.postorder(tree.root)  # 7 8 3 9 4 1 5 6 2 0
    print()

    # ====== Result ====== #
    # breadth travel:      #
    # 0 1 2 3 4 5 6 7 8 9  #
    # preorder:            #
    # 0 1 3 7 8 4 9 2 5 6  #
    # inorder:             #
    # 7 3 8 1 9 4 0 5 2 6  #
    # postorder:           #
    # 7 8 3 9 4 1 5 6 2 0  #
    #                      #
    # ==================== #

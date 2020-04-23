class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, value):
        self.root = BinaryNode(value)

    # 查找一个值
    def searchnode(self, value, node, parent, depth, nodetype):
        if node is None:
            return False, node, parent, depth, nodetype
        if value == node.value:
            return True, node, parent, depth, nodetype
        elif value < node.value:
            return self.searchnode(value, node.left, node, depth+1, 'leftchild')
        elif value > node.value:
            return self.searchnode(value, node.right, node, depth+1, 'rightchild')

    # 插入一个值
    def insert(self, value):
        flag, node, parent, depth, nodetype = self.searchnode(value, self.root, self.root, 0, None)
        if nodetype == 'leftchild':
            parent.left = BinaryNode(value)
        else:
            parent.right == BinaryNode(value)

    # 先序遍历
    def preTraverse(self, node):
        if node is None:
            return
        print(node.value)
        self.preTraverse(node.left)
        self.preTraverse(node.right)

    # 中序遍历
    def midTraverse(self, root):
        if root is None:
            return
        self.midTraverse(root.left)
        print(root.value)
        self.midTraverse(root.right)

    # 后序遍历
    def afterTraverse(self, root):
        if root is None:
           return
        self.afterTraverse(root.left)
        self.afterTraverse(root.right)
        print(root.value)

    def findmin(self, node):
        while node.left is not None:
            node = self.findmin(node.left)
        return node

    def findmax(self, node):
        while node.right is not None:
            node = self.findmax(node.right)
        return node

    def Remove(self, key):
        if self.root is None:
            raise KeyError("No such key found!")
        else:
            # 不断递归一层层向上返回删除更新后的节点，最上层是root
            self.root = self.remove(key, self.root)

    def remove(self, value, node):
        if node is None:
            return BinaryNode(value)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        elif value < node.value:
            node.left = self.remove(value, node.left)
        elif node.left and node.right:
            node.value = self.findmin(node.right)
            node = self.remove(node.value, node.right)
        else:
            if node.left:
                node = node.left
            else:
                node = node.right
        return node


if __name__ == '__main__':
    b = BinarySearchTree(10)
    b.insert(5)
    b.insert(15)
    b.insert(3)
    b.insert(8)
    b.insert(6)
    b.insert(9)
    b.insert(16)
    b.preTraverse(b.root)
    flag, *rest = b.searchnode(6, b.root, b.root, 0, None)
    print(flag)
    flag, *rest = b.searchnode(11, b.root, b.root, 0, None)
    print(flag)
    b.Remove(5)
    flag, *rest = b.searchnode(5, b.root, b.root, 0, None)
    print(flag)
    b.preTraverse(b.root)
















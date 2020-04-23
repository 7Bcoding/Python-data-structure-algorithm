class BinaryNode:
    def __init__(self, value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    # 前序遍历
    if root is None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    # 中序遍历
    if root is None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def aftertraverse(root):
    # 后序遍历
    if root is None:
        return
    aftertraverse(root.left)
    aftertraverse(root.right)
    print(root.value)


if __name__ == '__main__':
    root = BinaryNode('A')

    node1 = BinaryNode('B', BinaryNode('C'))
    node2 = BinaryNode('D', None, BinaryNode('E'))
    node1.right = node2
    root.left = node1

    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历：')
    aftertraverse(root)

    print(root)
    print(node1)
    print(node2)
    node1 = node1.right
    print(node1, node1.value)
    print(root, root.left, root.value)





class AVLNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def findmin(self, node):
        while node.left is not None:
            node = self.findmin(node.left)
        return node

    def findmax(self, node):
        while node.right is not None:
            node = self.findmax(node.right)
        return node

    def insert(self, value, node):
        if node is None:
            return AVLNode(value)
        elif value > node.value:
            node.right = self.insert(value, node.right)
        elif value < node.value:
            node.left = self.insert(value, node.left)
        else:
            None
        return self.balance(node)

    def Remove(self, key):
        if self.root is None:
            raise KeyError("No such key found!")
        else:
            self.root = self.remove(key, self.root)

    def remove(self, value, node):
        if node is None:
            return AVLNode(value)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        elif value < node.value:
            node.left = self.remove(value, node.left)
        elif node.left and node.right:
            if self.height(node.left) >= self.height(node.right):
                # 左比右高，那么右子树找最小的放上来做根
                k = self.findmin(node.right)
                node.value = k.value
                node.right = self.remove(k.value, node.right)
            else:
                # 左比右低，那么左子树找最大的放上来做根
                k = self.findmax(node.left)
                node.value = k.value
                node.left = self.remove(k.value, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            # 只有左孩子或右孩子或都没有
            if node.left:
                node = node.left
            else:
                # 叶子节点也算在此情况
                node = node.right
        return self.balance(node)

    def balance(self, node):
        if node is None:
            return node
        else:
            if (self.height(node.left) - self.height(node.right)) > 1:
                if self.height(node.left.left) >= self.height(node.left.right):
                    # 进行左节点单旋转
                    node = self.rotatewithleftChild(node)
                else:
                    # 进行双旋转
                    node = self.doublertleftChild(node)
            elif (self.height(node.right) - self.height(node.left)) > 1:
                if self.height(node.right.right) >= self.height(node.right.left):
                    # 进行右节点单旋转
                    node = self.rotatewithrightChild(node)
                else:
                    # 进行双旋转
                    node = self.doublertrightChild(node)
            node.height = max(self.height(node.left), self.height(node.right))+1
            return node

    def rotatewithleftchild(self, n2):
        n1 = n2.left
        n2.left = n1.right
        n1.right = n2
        # 交换值后计算深度
        n2.height = max(self.height(n2.left), self.height(n2.right))+1
        n1.height = max(self.height(n1.left), n2.height) + 1
        return n1

    def rotatewithrightchild(self, n1):
        n2 = n1.right
        n1.right = n2.left
        n2.left = n1
        n1.height = max(self.height(n1.left), self.height(n1.right))+1
        n2.height = max(self.height(n2.right), n1.height)+ 1
        return n2

    def doublertleftchild(self, n3):
        # 标准AVL双旋转，先右旋，再左旋
        n3.left = self.rotatewithrightchild(n3.left)
        return self.rotatewithleftchild(n3)

    def doublertrightchild(self, n3):
        # 标准AVL双旋转，先左旋，再右旋
        n3.right = self.rotatewithleftchild(n3.right)
        return self.rotatewithrightchild(n3)




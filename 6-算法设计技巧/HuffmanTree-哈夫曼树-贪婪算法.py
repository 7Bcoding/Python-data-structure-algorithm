'''
属于贪婪算法的经典应用案例之一：应用于文件压缩的哈夫曼编码算法
* 结点的权和带权路径长度：
  1.在许多应用中，常常将树中的结点赋予一个有着某种意义的实数，我们称此实数为该结点的权；
  2.结点的带权路径长度规定为从树根结点到该结点之间的路径长度与该结点上权的乘积.
* 哈夫曼树：哈夫曼树又称最优二叉树。它是 n 个带权叶子结点构成的所有二叉树中，带权路径长度 WPL 最小的二叉树
* 构建哈夫曼树：
  假设有n个权值，则构造出的哈夫曼树有n个叶子结点。 n个权值分别设为 w1、w2、…、wn，则哈夫曼树的构造规则为：
  1.将w1、w2、…，wn看成是有n棵树的森林(每棵树仅有一个结点)；
  2.在森林中选出两个根结点的权值最小的树合并，作为一棵新树的左、右子树，且新树的根结点权值为其左、右子树根结点权值之和；
  3.从森林中删除选取的两棵树，并将新树加入森林；
  4.重复(2)、(3)步，直到森林中只剩一棵树为止，该树即为所求得的哈夫曼树。
* 前缀编码（prefix code）
  1.利用字符集中每个字符的使用频率作为权值构造一个哈夫曼树；
  2.从根结点开始，为到每个叶子结点路径上的左分支赋予0，右分支赋予1，并从根到叶子方向形成该叶子结点的编码.
'''


class Node:
    def __init__(self, name, weight):
        self.name = name                                               # 节点名
        self.weight = weight                                           # 节点权重
        self.left = None                                               # 节点左孩子
        self.right = None                                              # 节点右孩子
        self.father = None                                             # 节点父节点

    # 判断是否是左孩子
    def is_left_child(self):
        return self.father.left == self


# 创建最初的叶子节点
def create_prim_nodes(data_set, labels):
    if len(data_set) != len(labels):
        raise Exception('数据和标签不匹配!')
    nodes = []
    for i in range(len(labels)):
        nodes.append( Node(labels[i], data_set[i]))
    return nodes


# 创建huffman树
def create_hf_tree(nodes):
    # 此处注意，copy()属于浅拷贝，只拷贝最外层元素，内层嵌套元素则通过引用，而不是独立分配内存
    tree_nodes = nodes.copy()
    while len(tree_nodes) > 1:                                         # 只剩根节点时，退出循环
        tree_nodes.sort(key=lambda node: node.weight)                  # 按权重升序排列
        new_left = tree_nodes.pop(0)
        new_right = tree_nodes.pop(0)
        new_node = Node(None, (new_left.weight + new_right.weight))
        new_node.left = new_left
        new_node.right = new_right
        new_left.father = new_right.father = new_node
        tree_nodes.append(new_node)
    tree_nodes[0].father = None                                        # 根节点父亲为None
    return tree_nodes[0]                                               # 返回根节点


# 获取huffman编码
def get_huffman_code(root, nodes):
    codes = {}
    for node in nodes:
        code=''
        name = node.name
        while node.father is not None:
            if node.is_left_child():
                code = '0' + code
            else:
                code = '1' + code
            node = node.father
        codes[name] = code
    return codes


if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd', 'e', 'f']
    data_set = [9, 12, 6, 3, 5, 15]
    nodes = create_prim_nodes(data_set, labels)                       # 创建初始叶子节点
    root = create_hf_tree(nodes)                                      # 创建huffman树
    codes = get_huffman_code(root, nodes)                             # 获取huffman编码

    for key in codes.keys():                                          # 打印huffman码
        print(key, ': ', codes[key])

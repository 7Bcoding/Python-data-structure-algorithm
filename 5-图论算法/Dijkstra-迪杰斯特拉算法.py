"""
问题：根据每条边的权值，求出从起点s到其他每个顶点的最短路径和最短路径的长度。
说明：不考虑权值为负的情况，否则会出现负值圈问题。
s：起点
v：算法当前分析处理的顶点
u：与v邻接的顶点
d：从s到v的距离
d(u)：从s到u的距离
e(v,u)：顶点v到顶点u的边的权值
问题分析：
Dijkstra算法按阶段进行，同无权最短路径算法（先对距离为0的顶点处理，再对距离为1的顶点处理，以此类推）
一样，都是先找距离最小的。在每个阶段，Dijkstra算法选择一个顶点v，它在所有unknown顶点中具有最小的d(v)。
同时算法声明从s到v的最短路径是known的。阶段的其余部分为，对w的d(v)距离）和 prev(上一个顶点)更新工作
（当然也可能不更新）。
在算法的每个阶段，都是这样处理的：
1.在无权的情况下，若du =无穷 则置d(u)=d(v)+1
2.在有权的情况下，若du =无穷 则置d(u)=d(v)+e(v,u)
3.若d(u)!=无穷，开始分析：从顶点v到顶点u的路径，若能使得u的路径长比u原来的路径长短一点，那么就需要对
u进行更新，否则不对u更新。即满足d(v) + e(v,u) < d(u)，就需要把d(u)的值更新为d(v) + e(v,u)，同时顶点u
的prev值改成顶点v
"""

global edges
global vlist
global vset


class Vertex:                              # 顶点类
    def __init__(self, vid, outlist):
        self.vid = vid                     # 出边
        self.outlist = outlist             # 出边指向的顶点id的列表，也可以理解为邻接表(只存储索引值，不存储顶点对象)
        self.known = False                 # 是否访问过
        self.dist = float('inf')           # s到该点的距离,默认为无穷大
        self.prev = 0                      # 上一个顶点的id，默认为0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vid == other.vid
        else:
            return False

    def __hash__(self):
        return hash(self.vid)              # 通过vid计算出顶点对象的哈希值，相同顶点对象具有相同的哈希值


def addEdge(front, back, value):           # 存储边的权值
    edges[(front, back)] = value


def reset():
    vset = set([v1, v2, v3, v4, v5, v6, v7])
    for i in range(1, len(vlist)):
        vlist[i].dist = float('inf')
        vlist[i].known = False
    return vset, vlist


def get_unknown_min():                     # 此函数则代替优先队列的出队操作
    min = 0
    index = 0
    flag = 0                               # 找到第一个unknown顶点的标志
    for i in range(1, len(vlist)):
        if vlist[i].known is True:         # 跳过所有known顶点
            continue
        else:
            if flag == 0:                  # 拿到第一个unknown顶点的权值，与其他unknown顶点作比较
                min = vlist[i].dist
                index = i
            else:
                if vlist[i].dist < min:
                    min = vlist[i].dist
                    index = i
            flag += 1
    # 此时已经找到了未知的最小的元素是谁
    vset.remove(vlist[index])              # 相当于执行出队操作
    return vlist[index]


def dijkstra(start):
    vlist[start].dist = 0
    while len(vset) != 0:
        v = get_unknown_min()
        v.known = True
        for u in v.outlist:
            if vlist[u].known is True:
                continue
            else:
                if vlist[u].dist == float('inf'):
                    vlist[u].dist = v.dist + edges[(v.vid, u)]
                    vlist[u].prev = v.vid
                if vlist[u].dist > (v.dist + edges[(v.vid, u)]):
                    vlist[u].dist = v.dist + edges[(v.vid, u)]
                    vlist[u].prev = v.vid
                else:
                    pass


def printpath(start, end):
    path = []
    path = getpath(start, end, path)
    length = 1
    spath = ''
    for s in path:
        if length >= len(path):
            last = s
            break
        spath = spath + 'v' + str(s) + '-->'
        length += 1
    spath = spath + 'v' + str(last)
    print('最短路径为 %s' % spath)
    print('该最短路径的长度为', vlist[end].dist)


def getpath(start, index, path):
    if index == start:
        path.insert(0, start)
        return path
    if vlist[index].dist == float('inf'):
        print('从起点到该顶点根本没有路径')
        return
    path.insert(0, index)
    path = getpath(start, vlist[index].prev, path)
    return path


if __name__ == '__main__':

    edges = dict()
    addEdge(1, 2, 2)
    addEdge(1, 4, 1)
    addEdge(3, 1, 4)
    addEdge(4, 3, 2)
    addEdge(2, 4, 3)
    addEdge(2, 5, 10)
    addEdge(4, 5, 2)
    addEdge(3, 6, 5)
    addEdge(4, 6, 8)
    addEdge(4, 7, 4)
    addEdge(7, 6, 1)
    addEdge(5, 7, 6)

    # 创建顶点对象
    v1 = Vertex(1, [2, 4])
    v2 = Vertex(2, [4, 5])
    v3 = Vertex(3, [1, 6])
    v4 = Vertex(4, [3, 5, 6, 7])
    v5 = Vertex(5, [7])
    v6 = Vertex(6, [])
    v7 = Vertex(7, [6])

    vlist = [False, v1, v2, v3, v4, v5, v6, v7]
    vset = set([v1, v2, v3, v4, v5, v6, v7])

    dijkstra(1)
    printpath(1, 3)
    printpath(1, 6)
    printpath(1, 5)

    vset, vlist = reset()
    dijkstra(2)
    printpath(2, 6)
    printpath(2, 7)

    vset, vlist = reset()
    dijkstra(4)
    printpath(4, 6)
    printpath(4, 7)

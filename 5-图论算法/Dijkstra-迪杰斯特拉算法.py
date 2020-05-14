from collections import defaultdict


# 顶点类
class Vertex:
    def __init__(self, vid, outlist):
        self.vid = vid  # 出边
        self.outlist = outlist  # 出边指向的顶点id的列表，也可以理解为邻接表(只存储索引值，不存储顶点对象)
        self.known = False  # 是否访问过
        self.dist = float('inf')  # s到该点的距离,默认为无穷大
        self.prev = 0  # 上一个顶点的id，默认为0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vid == other.vid
        else:
            return False

    def __hash__(self):
        return hash(self.vid)

#存储边的权值
def addEdge(front, back, edges, value):
    edges[front].insert(back, value)

def get_unknown_min(vlist):
    min = vlist[1]
    index = 0
    for i in range(1, len(vlist)):
        if vlist[i].known is True:
            continue
        else:
            if vlist[i].dist < min:
                min = vlist[i].dist
                index = i
    vset.remove(vlist[index])
    return vlist[index]

def dijkstra(vlist, vset, edges, start):
    vlist[start].dist = 0
    while len(vset) != 0:
        v = get_unknown_min()
        v.known = True
        for u in v.outlist:
            if vlist[u].known is True:
                continue
            else:
                if vlist[u].dist == float('inf'):
                    vlist[u].dist = v.dist + edges[v][u]
                    vlist[u].prev = v.dist
                if vlist[u].dist > (v.dist + edges[v][u]):
                    vlist[u].dist = v.dist + edges[v][u]
                    vlist[u].prev = v.dist
                else:
                    pass


def printpath(start, end):
    path = []
    path = getpath(start, end, start, path)
    spath = ''
    for s in range(0, len(path)-1):
        spath = 'V' + str(path(s)) + '-->'
    spath = spath + str(path[len(path-1)])
    print('最短路径为 %s', spath)
    print('该最短路径的长度为', vlist[end].dist)

def getpath(start, end, index, path):
    if index == start:
        path.insert(0, start)
        return path
    if vlist[index].dist == float('inf'):
        print('从起点到该顶点根本没有路径')
        return None
    path.insert(index)
    path = getpath(start, end, vlist[index].prev, path)
    return path


if __name__ == '__main__':

    edges = defaultdict(list)
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
    dijkstra(vlist, vset, edges, 1)
    printpath(1, 3)
    printpath(1, 6)

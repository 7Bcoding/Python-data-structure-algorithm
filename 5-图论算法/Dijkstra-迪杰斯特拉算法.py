from collections import defaultdict

class Vertex:
    def __init__(self, vid, outlist):
        self.vid = vid
        self.outlist = outlist
        self.known = False
        self.dist = float('inf')
        self.prev = 0

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
    min = 0
    index = 0
    for i in range(1, len(vlist)):
        if vlist[i].known is True:
            continue
        else:
            if vlist[i]

def dijkstra(vlist, vset, edges, start):

    vlist[start].dist = 0

    while len(vset) != 0:
        v = get_unknown_min()




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
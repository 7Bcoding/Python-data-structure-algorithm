from queue import Queue
from collections import defaultdict

'''
无权最短路径算法:
采取广度优先搜索的策略求顶点间的最短路径。具体过程如下：
  一些必要准备:
(1) 选取一个点s，例如上图的v2v2。我们求v2v2到所有其他顶点的最短路径。
(2) 借助一个标记每个顶点状态的信息表InfoTable，包含三个必要的信息：是否被遍历Known，
    与v2v2的距离dist，以及标记上一个经过的顶点的Path。下图为求v2v2的最短路径的状态表的初始化。
    Known=0表示没被遍历，dist无穷大表示初始其他顶点都不可达。 

主要步骤：
1.首先将目标顶点v2v2入队列。
2.当队列不为空时，执行循环：
3.顶点出队列，标记信息表中该顶点的状态Known=1（这个可以省去不要）。遍历该顶点的邻接表，当该顶点
  的邻接点的dist为无穷大时，更新它们的dist值为该顶点的dist+1，更新它们的Path值为该顶点。它们（该
  顶点的邻接点）入队列。
4.当队列为空时，遍历完v2v2的所有可达顶点。关于v2v2的状态表也更新完毕。读取状态表的Path栏，可以得到
  到所有顶点的最短路径。
  借助队列的无权最短路径算法的时间复杂度为O(|V|+|E|)。

'''


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 邻接表形式实现图-- 键:字典 , 值:列表(每个顶点指向的顶点)
        self.V = vertices               # 顶点数

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def unweighted(self, start, end):
        known = []
        dist = []
        prev = []
        q = Queue()
        dist[start] = 0
        q.put(start)
        while q:
            v = q.get()
            for u in self.graph[v]:
                prev[u] = v
                dist[u] += 1
                q.put(u)


if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 3)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 4)
    g.addEdge(5, 7)
    g.addEdge(7, 6)

    g.unweighted(1, 6)
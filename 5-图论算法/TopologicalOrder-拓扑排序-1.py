from collections import defaultdict

'''
在图论中，拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列，
该序列必须满足下列两个条件：
     1. 每个顶点仅出现一次
     2. 若存在一条从顶点 A 到顶点 B 的路径，那么在序列中顶点 A 出现在顶点 B 的前面。
只有有向无环图（DAG）才有拓扑一说，非DAG没有拓扑排序一说
那么如何对这个有向无环图（DAG）进行拓扑排序呢？
     1. 找出入度数为0的顶点
     2. 将入度数为0的顶点值取出，作为拓扑排序后列表的元素，再将该顶点指向的顶点入度减1
     3. 重复1,2步骤，直到图中没有入度为0且未被访问的顶点，得出的拓扑排序列表即为所求
'''


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 邻接表形式实现图-- 键:字典 , 值:列表(每个顶点指向的顶点)
        self.V = vertices               # 顶点数
        self.indegree = [0] * (vertices+1)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def indegcount(self):               # 计算所有节点的入度，放到一个列表中
        for u in self.graph:
            for v in self.graph[u]:
                self.indegree[v] += 1

    def topologicalsort(self):
        self.indegcount()
        queue = [u for u in self.graph if self.indegree[u] == 0]  # 查找所有入度为0的节点，并加入到队列中
        res = []
        while queue:
            u = queue.pop()                              # 不断将队列中入度为0的节点弹出
            res.append(u)                                # 每弹出一个入度为0 的节点，就加入到结果集中
            for v in self.graph[u]:
                self.indegree[v] -= 1                    # 将入度为0的节点指向的所有节点的入度减1
                if self.indegree[v] == 0:                # 减1后，指向的节点入度若为0，则加入队列
                    queue.append(v)
        return res


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

    print("拓扑排序结果：")
    res = g.topologicalsort()
    print(res)

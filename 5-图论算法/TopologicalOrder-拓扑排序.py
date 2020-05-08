from collections import defaultdict

'''
在图论中，拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列，该序列必须满足下列两个条件：
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
        self.graph = defaultdict(list) # 邻接表形式实现图-- 键:字典 , 值:列表(每个顶点指向的顶点)
        self.V = vertices  # 顶点数

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # 深度遍历的方式将入度最多的顶点先入栈，少的顶点先出栈，入度为0的顶点最先出栈
    def toposort(self, v, visited, stack):
        # 访问过的顶点标记为true
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.toposort(i, visited, stack)
        # 该顶点无任何出度，则入栈
        stack.insert(0, v)

    def topologicalsort(self):
        visited = [False] * (self.V+1)
        stack = []

        for i in range(1, self.V):
            # 访问过的顶点不再访问
            if visited[i] is False:
                self.toposort(i, visited, stack)

        print(stack)


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
    g.topologicalsort()
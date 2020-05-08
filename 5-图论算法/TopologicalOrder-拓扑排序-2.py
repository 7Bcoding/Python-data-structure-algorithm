from collections import defaultdict

'''
拓扑排序还有第二种实现方法，就是采用深度遍历的方式，不计算每个顶点的入度，直接深度遍历每个节点，
访问过的节点就标记为true，重复访问则跳过，遍历完该节点则加入到栈中，这样做的好处在于：可以高效
的把处于图中较深的节点先入栈（即那些入度较多的节点），入度较少的节点后入栈，不必再在入度数的计算
上耗费时间。最后将栈中元素弹出，即是入度少到入度多的顺序弹出，最先弹出的是入度为0的节点。
'''


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 邻接表形式实现图-- 键:字典 , 值:列表(每个顶点指向的顶点)
        self.V = vertices  # 顶点数

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # 深度遍历的方式将入度最多的顶点先入栈，较少的顶点后入栈，入度为0的顶点最先出栈
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
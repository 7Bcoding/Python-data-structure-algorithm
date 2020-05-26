'''
prim算法基本思路：
所有节点分成两个group，一组为已经选取的selected_node（为list类型），一组为candidate_node，
首先任取一个节点加入到selected_node，然后遍历头节点在selected_node，尾节点在candidate_node
的边，选取符合这个条件的边里权重最小的边，加入到最小生成树，选出的边的尾节点加入到selected_node，
并从candidate_node删除。直到candidate_node中没有备选节点（这个循环条件要求所有节点都有边连接，
即边数要大于等于节点数-1，循环开始前要加入这个条件判断，否则可能会有节点一直在candidate中，导致死循环）。

kruskal算法基本思路：
先对边按权重从小到大排序，再选取权重最小的一条边，若该边两个节点不在同一个连通分量中，则加入到最小生成树，
否则计算下一条边，直到遍历完所有的边。

连通分量：
无向图G的一个极大连通子图（即连通分量是图G中不被其他连通子图包含的连通子图，所以图G可以有多个连通分量）
称为原图G的一个连通分量（或连通分支）。连通图只有一个连通分量，即其自身；非连通的无向图有多个连通分量。
'''


class Graph(object):
    def __init__(self, maps):
        self.maps = maps                                         # 初始化邻接矩阵
        self.nodenum = self.get_nodenum()                        # 初始化节点数
        self.edgenum = self.get_edgenum()                        # 初始化边数

    # 获取节点数
    def get_nodenum(self):
        return len(self.maps)

    # 获取边数
    def get_edgenum(self):
        count = 0                                                       # 初始化边数
        for i in range(self.nodenum):
            for j in range(i):
                if 0 < self.maps[i][j] < 9999:                          # 生成边的条件是0<边的权重<9999
                    count += 1
        return count

    # prim算法
    def prim(self):
        res = []                                                        # 初始化最小生成树
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        seleted_node = [0]                                              # 初始化入围节点0，为起始节点，可任选
        candidate_node = [i for i in range(1, self.nodenum)]
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999                          # 初始化边的头节点、尾节点、最小权重
            for i in seleted_node:                                      # 遍历头节点在入围节点、尾节点在候选节点的边
                for j in candidate_node:
                    if self.maps[i][j] < minweight:                     # 若当前边的权重<最小权重，则更新
                        minweight = self.maps[i][j]                     # 更新最小权重值
                        begin = i                                       # 更新边的头节点
                        end = j                                         # 更新边的尾节点
            res.append([begin, end, minweight])                         # 将头节点、尾节点、最小权重添加到最小生成树中
            seleted_node.append(end)                                    # 将当前尾节点添加到入围节点中
            candidate_node.remove(end)                                  # 从候选节点中移除当前尾节点，然后继续循环
        return res

    # kruskal算法
    def kruskal(self):
        res = []                                                        # 初始化最小生成树
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:        # 若节点数<=0或边数<节点数-1，则
            return res
        edge_list = []                                                  # 初始化边列表
        for i in range(self.nodenum):
            for j in range(i + 1, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])           # 按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a: a[2])                              # 将边列表按权重的升序排序
        group = [[i] for i in range(self.nodenum)]                      # 生成可迭代的连通分量列表
        for edge in edge_list:                                          # 遍历边列表
            for i in range(self.nodenum):
                if edge[0] in group[i]:
                    m = i                                               # 当前边头节点在连通分量m中，m为连通分量列表的索引
                if edge[1] in group[i]:
                    n = i                                               # 当前边尾节点在连通分量n中，n为连通分量列表的索引
            if m != n:                                                  # 若该边的两个节点不在同一连通分量中，则
                res.append(edge)                                        # 将头节点、尾节点、最小权重添加到最小生成树中
                group[m] = group[m] + group[n]                          # 将连通分量列表的n合并到m中
                group[n] = []                                           # 清空连通分量列表n索引的连通分量
        return res


max_value = 9999
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]  # 邻接矩阵图
graph = Graph(maps)  # 实例化邻接矩阵
print('邻接矩阵为\n%s' % graph.maps)
print('节点数为%d，边数为%d。\n' % (graph.nodenum, graph.edgenum))
print('------最小生成树prim算法------')
print(graph.prim())
print('------最小生成树kruskal算法------')
print(graph.kruskal())

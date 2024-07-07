'''
SciPy 图结构
    图结构是算法学中最强大的框架之一。
    图是各种关系的节点和边的集合，节点是与对象对应的顶点，边是对象之间的连接。
    SciPy 提供了 scipy.sparse.csgraph 模块来处理图结构。
'''

# 连接组件
# 查看所有连接组件使用 connected_components() 方法。
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)
print(connected_components(newarr))

# Dijkstra -- 最短路径算法
# 查找元素 1 到 2 的最短路径：
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))


# Floyd-Warshall -- 弗洛伊德算法 所有最短路径算法
# 弗洛伊德算法算法是解决任意两点间的最短路径的一种算法。
# Scipy 使用 floyd_warshall() 方法来查找所有元素对之间的最短路径。

# 查找所有元素对之间的最短路径径：
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))

# Bellman Ford -- 贝尔曼-福特算法
# 贝尔曼-福特算法是解决任意两点间的最短路径的一种算法。
# Scipy 使用 bellman_ford() 方法来查找所有元素对之间的最短路径，通常可以在任何图中使用，包括有向图、带负权边的图。
# 使用负权边的图查找从元素 1 到元素 2 的最短路径：
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))


# 深度优先顺序
# depth_first_order() 方法从一个节点返回深度优先遍历的顺序。
# 给定一个邻接矩阵，返回深度优先遍历的顺序：
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

# 广度优先顺序
# breadth_first_order() 方法从一个节点返回广度优先遍历的顺序。
# 给定一个邻接矩阵，返回广度优先遍历的顺序：
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))

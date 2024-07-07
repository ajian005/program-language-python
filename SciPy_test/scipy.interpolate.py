'''
SciPy 插值
    什么是插值？
    在数学的数值分析领域中，插值（英语：interpolation）是一种通过已知的、离散的数据点，在范围内推求新数据点的过程或方法。
    简单来说插值是一种在给定的点之间生成点的方法。
'''
# 一维插值
# 一维数据的插值运算可以通过方法 interp1d() 完成。
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

'''
单变量插值
    在一维插值中，点是针对单个曲线拟合的，而在样条插值中，点是针对使用多项式分段定义的函数拟合的。
'''
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

'''
径向基函数插值
    径向基函数是对应于固定参考点定义的函数。
    曲面插值里我们一般使用径向基函数插值。
    Rbf() 函数接受 xs 和 ys 作为参数，并生成一个可调用函数，该函数可以用新的 xs 调用。
'''
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
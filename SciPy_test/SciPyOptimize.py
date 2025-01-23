'''
    SciPy 的 optimize 模块提供了常用的最优化算法函数实现，我们可以直接调用这些函数完成我们的优化问题，比如查找函数的最小值或方程的根等。
'''


# 查找 x + cos(x) 方程的根:
from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)
print("======myroot.x==========")
print(myroot.x)
# 查看更多信息
print("======myroot==========")
print(myroot)

'''
最小化函数
    函数表示一条曲线，曲线有高点和低点。
    高点称为最大值。
    低点称为最小值。
    整条曲线中的最高点称为全局最大值，其余部分称为局部最大值。
    整条曲线的最低点称为全局最小值，其余的称为局部最小值。
    可以使用 scipy.optimize.minimize() 函数来最小化函数。
'''
# x^2 + x + 2 使用 BFGS 的最小化函数:
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')
print("===========")
print(mymin)
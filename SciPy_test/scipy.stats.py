'''
Scipy 显著性检验
    显著性检验（significance test）就是事先对总体（随机变量）的参数或总体分布形式做出一个假设，然后利用样本信息来判断这个假设（备择假设）是否合理，即判断总体的真实情况与原假设是否有显著性差异。或者说，显著性检验要判断样本与我们对总体所做的假设之间的差异是纯属机会变异，还是由我们所做的假设与总体真实情况之间不一致所引起的。 显著性检验是针对我们对总体所做的假设做检验，其原理就是"小概率事件实际不可能性原理"来接受或否定假设。
    显著性检验即用于实验处理组与对照组或两种不同处理的效应之间是否有差异，以及这种差异是否显著的方法。
    SciPy 提供了 scipy.stats 的模块来执行Scipy 显著性检验的功能。
'''

'''
T 检验（T-Test）
        T 检验用于确定两个变量的均值之间是否存在显著差异，并判断它们是否属于同一分布。

        这是一个双尾测试。

        函数 ttest_ind() 获取两个相同大小的样本，并生成 t 统计和 p 值的元组。

        查找给定值 v1 和 v2 是否来自相同的分布：
'''
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

'''
KS 检验
    KS 检验用于检查给定值是否符合分布。
    该函数接收两个参数；测试的值和 CDF。
    CDF 为累积分布函数(Cumulative Distribution Function)，又叫分布函数。
    CDF 可以是字符串，也可以是返回概率的可调用函数。
    它可以用作单尾或双尾测试。
    默认情况下它是双尾测试。 我们可以将参数替代作为两侧、小于或大于其中之一的字符串传递。
    查找给定值是否符合正态分布：
'''
import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)

'''
    数据统计说明
        使用 describe() 函数可以查看数组的信息，包含以下值：
        nobs -- 观测次数
        minmax -- 最小值和最大值
        mean -- 数学平均数
        variance -- 方差
        skewness -- 偏度
        kurtosis -- 峰度
'''
import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)

'''
    正态性检验（偏度和峰度）
'''
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

'''
查找数据是否来自正态分布：
'''
import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))
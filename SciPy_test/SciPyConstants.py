'''
    SciPy 常量模块 constants 提供了许多内置的数学常数。
    圆周率是一个数学常数，为一个圆的周长和其直径的比率，近似值约等于 3.14159，常用符号  来表示。
'''
from scipy import constants

print(constants.pi)
print(constants.golden)

print(dir(constants))


from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21

# 二进制前缀
# 返回字节单位 (kibi 返回 1024)。
print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176

# 质量单位
# 返回多少千克 kg。(gram 返回 0.001)。
print(constants.gram)        #0.001
print(constants.metric_ton)  #1000.0
print(constants.grain)       #6.479891e-05
print(constants.lb)          #0.45359236999999997
print(constants.pound)       #0.45359236999999997
print(constants.oz)          #0.028349523124999998
print(constants.ounce)       #0.028349523124999998
print(constants.stone)       #6.3502931799999995
print(constants.long_ton)    #1016.0469088
print(constants.short_ton)   #907.1847399999999
print(constants.troy_ounce)  #0.031103476799999998
print(constants.troy_pound)  #0.37324172159999996
print(constants.carat)       #0.0002
print(constants.atomic_mass) #1.66053904e-27
print(constants.m_u)         #1.66053904e-27
print(constants.u)           #1.66053904e-27


# 角度单位
# 返回弧度 (degree 返回 0.017453292519943295)。
print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06

# 时间单位
# 返回秒数(hour 返回 3600.0)。
print(constants.minute)      #60.0
print(constants.hour)        #3600.0
print(constants.day)         #86400.0
print(constants.week)        #604800.0
print(constants.year)        #31536000.0
print(constants.Julian_year) #31557600.0

# 长度单位
# 返回米数(nautical_mile 返回 1852.0)。
print(constants.inch)              #0.0254
print(constants.foot)              #0.30479999999999996
print(constants.yard)              #0.9143999999999999
print(constants.mile)              #1609.3439999999998
print(constants.mil)               #2.5399999999999997e-05
print(constants.pt)                #0.00035277777777777776
print(constants.point)             #0.00035277777777777776
print(constants.survey_foot)       #0.3048006096012192
print(constants.survey_mile)       #1609.3472186944373
print(constants.nautical_mile)     #1852.0
print(constants.fermi)             #1e-15
print(constants.angstrom)          #1e-10
print(constants.micron)            #1e-06
print(constants.au)                #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)        #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16

# 压强单位
# 返回多少帕斯卡，压力的 SI 制单位。(psi 返回 6894.757293168361)。
print(constants.atm)         #101325.0
print(constants.atmosphere)  #101325.0
print(constants.bar)         #100000.0
print(constants.torr)        #133.32236842105263
print(constants.mmHg)        #133.32236842105263
print(constants.psi)         #6894.757293168361

# 面积单位
# 返回多少平方米，平方米是面积的公制单位，其定义是：在一平面上，边长为一米的正方形之面积。(hectare 返回 10000.0)。
print(constants.hectare) #10000.0
print(constants.acre)    #4046.8564223999992

# 体积单位
# 返回多少立方米，立方米容量计量单位，1 立方米的容量相当于一个长、宽、高都等于 1 米的立方体的体积，与 1 公秉和 1 度水的容积相等，也与1000000立方厘米的体积相等。(liter 返回 0.001)。
print(constants.liter)            #0.001
print(constants.litre)            #0.001
print(constants.gallon)           #0.0037854117839999997
print(constants.gallon_US)        #0.0037854117839999997
print(constants.gallon_imp)       #0.00454609
print(constants.fluid_ounce)      #2.9573529562499998e-05
print(constants.fluid_ounce_US)   #2.9573529562499998e-05
print(constants.fluid_ounce_imp)  #2.84130625e-05
print(constants.barrel)           #0.15898729492799998
print(constants.bbl)              #0.15898729492799998

# 速度单位
# 返回每秒多少米。(speed_of_sound 返回 340.5)。
print(constants.kmh)            #0.2777777777777778
print(constants.mph)            #0.44703999999999994
print(constants.mach)           #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot)           #0.5144444444444445

# 温度单位
# 返回多少开尔文。(zero_Celsius 返回 273.15)。
print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556

# 能量单位
# 返回多少焦耳，焦耳（简称焦）是国际单位制中能量、功或热量的导出单位，符号为J。(calorie 返回 4.184)。
print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556

# 功率单位
# 返回多少瓦特，瓦特（符号：W）是国际单位制的功率单位。1瓦特的定义是1焦耳/秒（1 J/s），即每秒钟转换，使用或耗散的（以安培为量度的）能量的速率。(horsepower 返回 745.6998715822701)。
print(constants.hp)         #745.6998715822701
print(constants.horsepower) #745.6998715822701

# 力学单位
# 返回多少牛顿，牛顿（符号为N，英语：Newton）是一种物理量纲，是力的公制单位。它是以建立经典力学（经典力学）的艾萨克·牛顿命名。。(kilogram_force 返回 9.80665)。
print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665






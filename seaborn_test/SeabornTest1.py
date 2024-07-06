'''
  使用 Seaborn 和 Matplotlib 绘制了一个简单的柱状图，用于展示不同产品的销售情况
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题和颜色调色板
sns.set_theme(style="darkgrid", palette="pastel")

# 示例数据
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [120, 210, 150, 180]

# 创建柱状图
sns.barplot(x=products, y=sales)

# 添加标签和标题
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales of Different Products")

# 显示图形
plt.show()
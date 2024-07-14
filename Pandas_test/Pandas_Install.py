import pandas
import pandas as pd

print(pd.__version__)

# 一个简单的 pandas 实例
import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
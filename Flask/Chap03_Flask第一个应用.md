## Flask 第一个应用
上一章节我们已经成功安装了 Flask，接下来我们可以创建一个简单的 Flask 应用。

首先，创建一个名为 app.py 的文件，并添加以下内容：

实例
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```
在命令行中运行 Flask 应用：
```shell
python app.py
```
你会看到 Flask 开发服务器启动，并显示类似于以下内容：
```
...
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 977-918-914
...
```
打开浏览器，访问 http://127.0.0.1:5000/，应该会看到 "Hello, World!" 的消息，表示 Flask 已成功安装并运行。



## 代码解析：
from flask import Flask： 这行代码从 flask 模块中导入了 Flask 类。Flask 类是 Flask 框架的核心，用于创建 Flask 应用程序实例。

app = Flask(__name__)： 这行代码创建了一个 Flask 应用实例。__name__ 是一个特殊的 Python 变量，它在模块被直接运行时是 '__main__'，在被其他模块导入时是模块的名字。传递 __name__ 给 Flask 构造函数允许 Flask 应用找到和加载配置文件。

@app.route('/')： 这是一个装饰器，用于告诉 Flask 哪个 URL 应该触发下面的函数。在这个例子中，它指定了根 URL（即网站的主页）。

def hello_world():： 这是定义了一个名为 hello_world 的函数，它将被调用当用户访问根URL时。

return 'Hello, World!'： 这行代码是 hello_world 函数的返回值。当用户访问根 URL 时，这个字符串将被发送回用户的浏览器。

if __name__ == '__main__':：这行代码是一个条件判断，用于检查这个模块是否被直接运行，而不是被其他模块导入。如果是直接运行，下面的代码块将被执行。

app.run(debug=True)：这行代码调用 Flask 应用实例的 run 方法，启动 Flask 内置的开发服务器。debug=True 参数会启动调试模式，这意味着应用会在代码改变时自动重新加载，并且在发生错误时提供一个调试器。
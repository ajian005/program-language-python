# Flask 路由
Flask 路由是 Web 应用程序中将 URL 映射到 Python 函数的机制。

Flask 路由是 Flask 应用的核心部分，用于处理不同 URL 的请求，并将请求的处理委托给相应的视图函数。

以下是关于 Flask 路由的详细说明，包括路由的定义、参数、方法和规则等。

1 定义路由：使用 @app.route('/path') 装饰器定义 URL 和视图函数的映射。
2 路由参数：通过动态部分在 URL 中传递参数。
3 路由规则：使用类型转换器指定 URL 参数的类型。
4 请求方法：指定允许的 HTTP 请求方法。
5 路由函数返回：视图函数可以返回不同类型的响应。
6 静态文件和模板：管理静态文件和动态渲染 HTML 模板。
7 路由优先级：确保路由顺序正确，以避免意外的匹配结果。

## 1. 定义路由
基本路由定义：

实例
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'
```

@app.route('/')：装饰器，用于定义路由。/ 表示根 URL。
def home()：视图函数，当访问根 URL 时，返回 'Welcome to the Home Page!'。

## 2. 路由参数
路由可以包含动态部分，通过在路由中指定参数，可以将 URL 中的部分数据传递给视图函数。

实例
```python
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'
```
## 3. 路由规则
路由规则支持不同类型的参数和匹配规则。

类型规则：

字符串（默认）： 匹配任意字符串。
整数（<int:name>）： 匹配整数值。
浮点数（<float:value>）： 匹配浮点数值。
路径（<path:name>）： 匹配任意字符，包括斜杠 /。
实例
```python
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f'User ID: {user_id}'

@app.route('/files/<path:filename>')
def serve_file(filename):
    return f'Serving file: {filename}'
@app.route('/user/<int:user_id>')：匹配整数类型的 user_id。
@app.route('/files/<path:filename>')：匹配包含斜杠的路径 filename。
```
## 4. 请求方法
Flask 路由支持不同的 HTTP 请求方法，如 GET、POST、PUT、DELETE 等。可以通过 methods 参数指定允许的请求方法。

实例
```python
@app.route('/submit', methods=['POST'])
def submit():
    return 'Form submitted!'
```
## 5. 路由转换器
Flask 提供了一些内置的转换器，可以对 URL 中的参数进行特定类型的转换。

常用转换器：

int： 匹配整数。
float： 匹配浮点数。
path： 匹配任意路径，包括斜杠。
实例
```python
@app.route('/items/<int:item_id>/details')
def item_details(item_id):
    return f'Item details for item ID: {item_id}'
```
<int:item_id>：将 URL 中的 item_id 转换为整数。
## 6. 路由函数返回
视图函数可以返回多种类型的响应：

字符串：返回纯文本响应。
HTML：返回 HTML 页面。
JSON：返回 JSON 数据。
Response 对象：自定义响应。
实例
```python
from flask import jsonify, Response

@app.route('/json')
def json_response():
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/custom')
def custom_response():
    response = Response('Custom response with headers', status=200)
    response.headers['X-Custom-Header'] = 'Value'
    return response
```
jsonify(data)：将字典转换为 JSON 响应。
Response('Custom response with headers', status=200)：创建自定义响应对象。
## 7. 静态文件和模板
静态文件（如 CSS、JavaScript、图片）可以通过 static 路由访问。模板文件则通过 templates 文件夹组织，用于渲染 HTML 页面。

静态文件访问：
```python
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
实例
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```
模板文件渲染：

实例
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```
模板文件 (templates/hello.html)：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```
## 8. 路由优先级
Flask 按照定义的顺序匹配路由，第一个匹配成功的路由将被处理。确保更具体的路由放在更一般的路由之前。

实例
```python
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f'User ID: {user_id}'

@app.route('/user')
def user_list():
    return 'User List'
```
/user/123 将匹配到 /user/<int:user_id>，而 /user 将匹配到 user_list。
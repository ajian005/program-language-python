# Flask 错误处理
Flask 提供了灵活的错误处理机制，可以捕获并处理应用中的各种错误。

以下是详细的说明，涵盖了如何定义和处理错误，如何处理 HTTP 状态码以及如何处理自定义错误。

处理 HTTP 错误：使用 @app.errorhandler 装饰器定义针对特定 HTTP 状态码的错误处理函数。
蓝图中的错误处理：在蓝图中定义错误处理函数，允许模块化的错误处理。
自定义错误：定义自定义异常类，并在应用中捕获和处理这些异常。
全局错误处理：使用全局错误处理函数捕获所有未处理的异常。
使用 abort 函数：在视图函数中主动触发 HTTP 错误。
渲染自定义错误页面：为每个错误码创建自定义的 HTML 错误页面。
## 1. 处理 HTTP 错误
Flask 允许你定义针对特定 HTTP 状态码的错误处理函数。这些处理函数可以用于捕获并处理应用中的常见错误，如 404 页面未找到错误、500 服务器内部错误等。

app.py 文件代码：

实例
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the homepage!'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```
@app.errorhandler(404)：捕获 404 错误，并返回自定义的 404 错误页面。

@app.errorhandler(500)：捕获 500 错误，并返回自定义的 500 错误页面。

## 2. 使用蓝图中的错误处理
蓝图（Blueprints）也可以定义自己的错误处理函数。这使得每个模块可以有自己的错误处理逻辑。

auth/routes.py 文件代码：

实例
```python
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.errorhandler(404)
def auth_not_found(error):
    return render_template('auth_404.html'), 404
```
app.py 文件代码：

实例
```python
from flask import Flask
from auth.routes import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
```
## 3. 处理自定义错误
你可以定义自定义异常类，并在应用中捕获和处理这些异常。这允许你在应用中实现更复杂的错误处理逻辑。

自定义异常类：

class CustomError(Exception):
    pass
抛出自定义异常：
```pyton
@app.route('/raise_custom_error')
def raise_custom_error():
    raise CustomError("This is a custom error.")
```
处理自定义异常：

@app.errorhandler(CustomError)
def handle_custom_error(error):
    return str(error), 400
## 4. 全局错误处理
如果你希望在整个应用中处理所有未处理的异常，可以使用全局错误处理函数。这些处理函数可以捕获所有未被显式捕获的错误。

app.py 文件代码：

实例
```python
@app.errorhandler(Exception)
def handle_exception(error):
    # 处理所有异常
    return f'An error occurred: {error}', 500
```
## 5. 使用 abort 函数
Flask 提供了一个 abort 函数，用于在视图函数中主动触发 HTTP 错误。这可以用于在特定条件下返回错误响应。

实例
```
from flask import abort

@app.route('/abort_example')
def abort_example():
    abort(403)  # 返回 403 Forbidden 错误
```
abort(403)：触发 403 错误，自动调用对应的错误处理函数。

## 6. 渲染自定义错误页面
可以为每个错误码创建自定义的 HTML 页面，使得错误页面与应用的整体设计一致。

项目结构示例：
```
yourapp/
│
├── app.py
├── templates/
│   ├── 404.html
│   ├── 500.html
│   └── auth_404.html
```
自定义错误页面示例：

templates/404.html 文件代码：

实例
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```
# Flask 模板渲染
模板是包含占位符的 HTML 文件。

Flask 使用 Jinja2 模板引擎来处理模板渲染。模板渲染允许你将动态内容插入到 HTML 页面中，使得应用能够生成动态的网页内容。

以下是关于 Flask 模板渲染的详细说明，包括如何创建和使用模板、模板继承、控制结构等。

创建模板：将 HTML 文件放在 templates 文件夹中，使用 Jinja2 占位符。
渲染模板：使用 render_template 函数在视图函数中渲染模板。
模板继承：创建基础模板，允许其他模板继承和扩展。
控制结构：使用条件语句和循环在模板中控制逻辑。
过滤器：使用过滤器格式化变量数据。
宏和模板包含：创建和使用宏以及模板包含，提高模板的复用性。
安全性：Jinja2 默认对模板变量进行自动转义以防止 XSS 攻击。
模板上下文：将数据传递给模板，并在模板中使用这些数据。
## 1. 基本概念
模板是包含占位符的 HTML 文件。

Flask 使用 Jinja2 模板引擎来渲染这些模板，将 Python 数据插入到 HTML 中，从而生成最终的网页。

## 2. 创建模板
模板文件通常放在项目的 templates 文件夹中。

Flask 会自动从这个文件夹中查找模板文件。

创建模板文件：在项目目录下创建 templates 文件夹，并在其中创建一个 HTML 文件，如 index.html。

templates/index.html 文件代码：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>Hello, {{ name }}!</p>
</body>
</html>
```
{{ title }} 和 {{ name }} 是模板占位符，将在渲染时被替换成实际的值。

在视图函数中渲染模板：

app.py 文件代码：

实例
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Welcome Page', name='John Doe')

if __name__ == '__main__':
    app.run(debug=True)
```
render_template('index.html', title='Welcome Page', name='John Doe')：渲染 index.html 模板，并将 title 和 name 变量传递给模板。

## 3. 模板继承
模板继承允许你创建一个基础模板，然后在其他模板中继承和扩展这个基础模板，避免重复的 HTML 代码。

创建基础模板：在 templates 文件夹中创建一个基础模板 base.html。

templates/base.html 示例：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>Footer content</p>
    </footer>
</body>
</html>
```
{% block title %}{% endblock %} 和 {% block content %}{% endblock %} 是定义的可替换区域。

创建子模板：在 templates 文件夹中创建一个子模板 index.html，继承 base.html。

templates/index.html 文件代码：

实例
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h2>Welcome to the Home Page!</h2>
<p>Content goes here.</p>
{% endblock %}
```
{% extends "base.html" %}：继承基础模板。

{% block title %} 和 {% block content %}：重写基础模板中的块内容。

## 4. 控制结构
Jinja2 提供了多种控制结构，用于在模板中实现条件逻辑和循环。

条件语句：

实例
```html
{% if user %}
    <p>Welcome, {{ user }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```
{% if user %}：检查 user 变量是否存在，如果存在，则显示欢迎消息，否则显示登录提示。

循环语句：

实例
```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```
{% for item in items %}：遍历 items 列表，并为每个项生成一个 <li> 元素。

## 5. 过滤器
过滤器用于在模板中格式化和处理变量数据。
```html
<p>{{ name|capitalize }}</p>
<p>{{ price|round(2) }}</p>
```
{{ name|capitalize }}：将 name 变量的值首字母大写。

{{ price|round(2) }}：将 price 变量的值四舍五入到小数点后两位。

## 6. 宏和模板包含
宏是可重用的模板片段。模板包含允许你在一个模板中插入另一个模板的内容。

创建宏
templates/macros.html 代码文件：

实例
```html
{% macro render_item(item) %}
    <div>
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
    </div>
{% endmacro %}
```
使用宏：

templates/index.html 文件代码：

实例
```html
{% from "macros.html" import render_item %}

<h1>Items</h1>
{% for item in items %}
    {{ render_item(item) }}
{% endfor %}
```
{% from "macros.html" import render_item %}：导入宏。

{{ render_item(item) }}：调用宏来渲染每个 item。

## 7. 安全性
自动转义：Jinja2 默认会对模板中的变量进行自动转义，防止 XSS 攻击。
```html
<p>{{ user_input }}</p>
```
{{ user_input }}：用户输入的内容会被自动转义，以避免恶意脚本的注入。

## 8. 模板上下文
视图函数中传递的变量成为模板的上下文，这些变量可以在模板中直接使用。

实例
```html
@app.route('/profile/<username>')
def profile(username):
    user = {'name': username, 'age': 25}
    return render_template('profile.html', user=user)
```
templates/profile.html 文件代码：

实例
```html
<h1>{{ user.name }}</h1>
<p>Age: {{ user.age }}</p>
```
{{ user.name }} 和 {{ user.age }}：在模板中访问 user 变量的属性。
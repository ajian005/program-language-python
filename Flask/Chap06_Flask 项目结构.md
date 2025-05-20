# Flask 项目结构
一个 Flask 应用可以简单到只有一个文件。

比如以下 hello.py 文件就是一个 Flask 应用：

实例
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```
然而，当项目变大时，把所有代码都放到一个文件里不太现实。

Flask 项目结构可以根据应用的规模和复杂性有所不同。

以下是几种常见的 Flask 项目结构，分别适用于简单应用和较复杂的应用。

简单项目结构：适用于小型应用，所有代码集中在一个文件中。
中型项目结构：将应用分为多个模块，便于管理和扩展。
复杂项目结构：支持更高的模块化，适用于大型应用，包含路由、模型、模板和静态文件目录。
## 1. 简单项目结构
对于一个简单的 Flask 应用，项目结构可以非常简洁：
```
my_flask_app/
│
├── app.py
└── requirements.txt
```
app.py：主要的 Flask 应用文件，包含路由和视图函数的定义。
requirements.txt：列出项目的依赖库，用于记录 Flask 和其他包的版本信息。
my_flask_app 目录下的 app.py 文件代码：

实例
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```
requirements.txt 示例：
```
Flask==2.2.3
```

## 2. 中型项目结构
对于稍复杂的应用，通常会将项目分为多个模块和目录：
```
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
│
├── config.py
├── requirements.txt
└── run.py
```
app/：包含 Flask 应用的主要代码。
__init__.py：初始化 Flask 应用和配置扩展。
routes.py：定义应用的路由和视图函数。
models.py：定义应用的数据模型。
config.py：配置文件，包含应用的配置信息。
requirements.txt：列出项目的依赖库。
run.py：用于启动 Flask 应用。
app/__init__.py 示例：

实例
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from . import routes
    app.register_blueprint(routes.bp)

    return app
```
app/routes.py 示例：

实例
```python
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return 'Hello, World!'
```
run.py 示例：

实例
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```
## 3. 复杂项目结构
对于较大的应用，可能需要更复杂的项目结构，以支持更高的模块化和扩展性：
```
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── auth.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── templates/
│   │   ├── layout.html
│   │   └── home.html
│   └── static/
│       ├── css/
│       └── js/
│
├── config.py
├── requirements.txt
├── migrations/
│   └── ...
└── run.py
```
app/routes/：将不同功能模块的路由分开管理。
main.py：主模块的路由。
auth.py：认证相关的路由。
app/models/：管理数据模型，通常与数据库操作相关。
user.py：用户模型。
app/templates/：存放 HTML 模板文件。
app/static/：存放静态文件，如 CSS 和 JavaScript。
migrations/：数据库迁移文件，通常与 SQLAlchemy 相关。
app/routes/main.py 示例：

实例
```python
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')
```
app/models/user.py 示例：

实例
```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
```
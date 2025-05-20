# Flask 数据库操作
在 Flask 中，数据库操作是构建 Web 应用的一个重要方面。

Flask 提供了多种方式来与数据库进行交互，包括直接使用 SQL 和利用 ORM（对象关系映射）工具，如 SQLAlchemy。

以下是对 Flask 数据库操作的详细说明，包括使用 SQLAlchemy 的基本操作和 SQL 语句的直接执行。

使用 SQLAlchemy：定义模型，配置数据库，执行基本的 CRUD 操作。
创建和管理数据库：使用 db.create_all() 创建表。
CRUD 操作：添加、读取、更新和删除记录。
查询操作：执行基本和复杂查询，包括排序和分页。
Flask-Migrate：使用 Flask-Migrate 管理数据库迁移。
执行原始 SQL：使用原始 SQL 语句进行数据库操作。
## 1. 使用 SQLAlchemy
SQLAlchemy 是一个强大的 ORM 库，可以简化数据库操作，通过 Python 对象与数据库表进行交互。

Flask-SQLAlchemy 是 Flask 的一个扩展，用于集成 SQLAlchemy。

安装 Flask-SQLAlchemy
```
pip install flask-sqlalchemy
```
配置 SQLAlchemy
app.py 文件代码：

实例
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # 使用 SQLite 数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```
## 2. 定义模型
模型是数据库表的 Python 类，每个模型类代表数据库中的一张表。

实例
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```
db.Model：所有模型类需要继承自 db.Model。

db.Column：定义模型的字段，指定字段的类型、是否为主键、是否唯一、是否可以为空等属性。

## 3. 创建和管理数据库
创建数据库和表
在定义了模型后，你可以使用 SQLAlchemy 提供的方法来创建数据库和表。
```
with app.app_context():
    db.create_all()
```
db.create_all()：创建所有在当前上下文中定义的模型对应的表。

## 4. 基本的 CRUD 操作
创建记录
实例
```python
@app.route('/add_user')
def add_user():
    new_user = User(username='john_doe', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    return 'User added!'
```
db.session.add(new_user)：将新用户对象添加到会话中。

db.session.commit()：提交事务，将更改保存到数据库。

读取记录
实例
```python
@app.route('/get_users')
def get_users():
    users = User.query.all()  # 获取所有用户
    return '<br>'.join([f'{user.username} ({user.email})' for user in users])
```
User.query.all()：查询所有用户记录。

更新记录
实例
```python
@app.route('/update_user/<int:user_id>')
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.username = 'new_username'
        db.session.commit()
        return 'User updated!'
    return 'User not found!'
```
User.query.get(user_id)：通过主键查询单个用户记录。

更新字段值并提交事务。

删除记录
实例
```python
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User deleted!'
    return 'User not found!'
```
db.session.delete(user)：删除用户记录，并提交事务。

## 5. 查询操作
SQLAlchemy 提供了丰富的查询功能，可以通过查询对象来执行各种查询操作。

基本查询
```
users = User.query.filter_by(username='john_doe').all()
```
filter_by()：根据字段值过滤记录。

复杂查询
```
from sqlalchemy import or_

users = User.query.filter(or_(User.username == 'john_doe', User.email == 'john@example.com')).all()
```
or_()：用于执行复杂的查询条件。

排序和分页
```
users = User.query.order_by(User.username).paginate(page=1, per_page=10)
```
order_by()：按指定字段排序。

paginate()：分页查询。

## 6. 使用 Flask-Migrate 进行迁移
Flask-Migrate 是一个用于数据库迁移的扩展，基于 Alembic，可以帮助你管理数据库的版本控制。

安装 Flask-Migrate
```
pip install flask-migrate
```
配置 Flask-Migrate
app.py 文件代码：
```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```
初始化迁移
```
flask db init
```
创建迁移脚本
```
flask db migrate -m "Initial migration."
```
应用迁移
flask db upgrade
flask db init：初始化迁移环境。
flask db migrate -m "message"：创建迁移脚本。
flask db upgrade：应用迁移到数据库。
## 7. 执行原始 SQL
虽然 SQLAlchemy 提供了 ORM 功能，但你也可以执行原始 SQL 语句。

实例
```python
@app.route('/raw_sql')
def raw_sql():
    result = db.session.execute('SELECT * FROM user')
    return '<br>'.join([str(row) for row in result])
```
db.session.execute()：执行原始 SQL 查询。

## Flask 中连接和操作 MySQL 数据库
在 Flask 中连接和操作 MySQL 数据库通常涉及到使用 SQLAlchemy 或直接使用 MySQL 的 Python 驱动。以下是详细的步骤，包括使用 Flask-SQLAlchemy 和直接使用 MySQL 的 Python 驱动进行操作。

### 1. 使用 Flask-SQLAlchemy 连接 MySQL
Flask-SQLAlchemy 是 Flask 的一个扩展，它简化了 SQLAlchemy 的配置和操作。要连接 MySQL，你需要安装 Flask-SQLAlchemy 和 MySQL 驱动。

安装必要的库：
```
pip install flask-sqlalchemy mysqlclient
```
flask-sqlalchemy：Flask 的 SQLAlchemy 扩展。
mysqlclient：MySQL 数据库的 Python 驱动。
### 配置 Flask-SQLAlchemy
app.py 文件代码：

实例
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```
code>SQLALCHEMY_DATABASE_URI：设置数据库连接 URI，格式为 mysql://username:password@localhost/dbname。

username：MySQL 用户名。
password：MySQL 密码。
localhost：MySQL 主机地址（本地通常为 localhost）。
dbname：数据库名称。
### 定义模型和执行基本操作
app.py 文件代码：

实例
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    users = User.query.all()
    return '<br>'.join([f'{user.username} ({user.email})' for user in users])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(debug=True)
```
### 直接使用 MySQL 的 Python 驱动
如果你选择不使用 SQLAlchemy，而直接使用 MySQL 的 Python 驱动，你可以使用 mysql-connector-python 或 PyMySQL 库。

安装 mysql-connector-python：
```
pip install mysql-connector-python
```
安装 PyMySQL（如果选择使用 PyMySQL）：
```
pip install PyMySQL
```
#### 使用 mysql-connector-python 连接 MySQL

app.py 文件代码：

实例
```python
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='username',
        password='password',
        database='dbname'
    )
    return connection

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user (username, email) VALUES (%s, %s)', (name, email))
    connection.commit()
    cursor.close()
    connection.close()

    return 'User added!'

@app.route('/get_users')
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```
使用 PyMySQL 连接 MySQL，app.py 文件代码：

实例
```python
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='username',
        password='password',
        database='dbname',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO user (username, email) VALUES (%s, %s)', (name, email))
        connection.commit()

    connection.close()
    return 'User added!'

@app.route('/get_users')
def get_users():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()

    connection.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```
from flask import Flask 
from flask import request
from flask import make_response
from flask import render_template
from flask import Blueprint



app = Flask(__name__)

'''
1. 路由 (Routing)
    路由是 URL 到 Python 函数的映射。Flask 允许你定义路由，使得当用户访问特定 URL 时，Flask 会调用对应的视图函数来处理请求。
'''
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About Page'

'''
2. 视图函数 (View Functions)
    视图函数是处理请求并返回响应的 Python 函数。它们通常接收请求对象作为参数，并返回响应对象，或者直接返回字符串、HTML 等内容。
'''
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

'''
3. 请求对象 (Request Object)
    请求对象包含了客户端发送的请求信息，包括请求方法、URL、请求头、表单数据等。Flask 提供了 request 对象来访问这些信息。
'''
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello, {username}'


def test_submit_route():
    # 创建测试客户端
    client = app.test_client()
    
    # 测试正常请求
    response = client.post('/submit', data={'username': 'Alice'})
    assert response.status_code == 200
    assert b'Hello, Alice' in response.data
    
    # 测试无参数请求
    response = client.post('/submit')
    assert response.status_code == 200
    assert b'Hello, None' in response.data
    
    # 测试空用户名
    response = client.post('/submit', data={'username': ''})
    assert response.status_code == 200
    assert b'Hello, ' in response.data

    print("所有测试用例通过!")


'''
4. 响应对象 (Response Object)
    响应对象包含了发送给客户端的响应信息，包括状态码、响应头和响应体。Flask 默认会将字符串、HTML 直接作为响应体。
'''
def  custom_response():
    response = make_response('This is a custom response')
    response.headers['X-Custom-Header'] = 'Custom Value'
    return response

'''
5. 模板 (Templates)
    Flask 使用 Jinja2 模板引擎来渲染 HTML 模板。模板允许你将 Python 代码嵌入到 HTML 中，从而动态生成网页内容。
'''
@app.route('/hello/<name>')

def  hello(name):
    return render_template('hello.html', name=name)

'''
6. 应用工厂 (Application Factory)
    应用工厂是一个 Python 函数，用于创建和配置 Flask 应用实例。这种方法允许你创建多个应用实例，或者在不同配置下初始化应用。
'''
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    from . import routes
    app.register_blueprint(routes.bp)
    return app

'''
7. 配置对象 (Configuration Objects)
    配置对象用于设置应用的各种配置选项，如数据库连接字符串、调试模式等。可以通过直接设置或加载配置文件来配置 Flask 应用。
'''
class Config:
    DEBUG = True
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'


'''
8. 蓝图 (Blueprints)
    蓝图是 Flask 中的组织代码的方式。它允许你将相关的视图函数、模板和静态文件组织在一起，并且可以在多个应用中重用。
'''
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return 'Home Page'

'''
注册蓝图 (app/__init__.py)：
    from flask import Flask
    from .routes import bp as main_bp

    def create_app():
        app = Flask(__name__)
        app.register_blueprint(main_bp)
        return app
'''

'''
9. 静态文件 (Static Files)
    静态文件是不会被服务器端执行的文件，如 CSS、JavaScript 和图片文件。Flask 提供了一个简单的方法来服务这些文件。

    访问静态文件示例：

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    静态文件目录：将静态文件放在 static 文件夹中，Flask 会自动提供服务。
'''


'''
10. 扩展 (Extensions)
    Flask 有许多扩展，可以添加额外的功能，如数据库集成、表单验证、用户认证等。这些扩展提供了更高级的功能和第三方集成。

    from flask_sqlalchemy import SQLAlchemy

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    db = SQLAlchemy(app)
'''


'''
11. 会话 (Sessions)
    Flask 使用客户端会话来存储用户信息，以便在用户浏览应用时记住他们的状态。会话数据存储在客户端的 cookie 中，并在服务器端进行签名和加密。

    实例
    from flask import session

    # 自动生成的密钥
    app.secret_key = 'your_secret_key_here'

    @app.route('/set_session/<username>')
    def set_session(username):
        session['username'] = username
        return f'Session set for {username}'

    @app.route('/get_session')
    def get_session():
        username = session.get('username')
        return f'Hello, {username}!' if username else 'No session data'
    session 对象用于存取会话数据。

    你可以使用 Python 内置的 secrets 模块生成一个强随机性的密钥。

    python3 -c 'import secrets; print(secrets.token_hex())'

'''


'''
12. 错误处理 (Error Handling)
    Flask 允许你定义错误处理函数，当特定的错误发生时，这些函数会被调用。可以自定义错误页面或处理逻辑。

    实例
    @app.errorhandler(404)
    def page_not_found(e):
        return 'Page not found', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return 'Internal server error', 500
    @app.errorhandler(404)：定义 404 错误的处理函数，返回自定义错误页面。
'''



'''
    if __name__ == '__main__':
        test_submit_route()
'''
if __name__ == '__main__':
    app.run(debug=True)
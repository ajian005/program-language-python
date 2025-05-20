# Flask 表单处理
在 Flask 中，表单处理是构建 Web 应用时一个常见的需求。

处理表单数据涉及到接收、验证和处理用户提交的表单。Flask 提供了基本的表单处理功能，但通常结合 Flask-WTF 扩展来简化表单操作和验证。

基本表单处理：使用 request.form 获取表单数据。
使用 Flask-WTF：结合 WTForms 进行表单处理和验证，简化表单操作。
表单验证：使用验证器确保表单数据的有效性。
文件上传：处理文件上传和保存文件。
CSRF 保护：确保表单免受跨站请求伪造攻击。
## 1. 基本表单处理
Flask 提供了直接处理表单数据的方式，使用 request 对象来获取提交的数据。

创建 HTML 表单
templates/form.html 文件代码：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
action="/submit"：表单数据提交到 /submit 路径。

method="post"：使用 POST 方法提交数据。

处理表单数据
app.py 文件代码：

实例
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f'Name: {name}, Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
```
request.form.get('name') 和 request.form.get('email')：获取提交的表单数据。

## 2. 使用 Flask-WTF 扩展
Flask-WTF 是一个封装了 WTForms 的扩展，提供了表单处理和验证的功能，使得表单处理更加简洁和强大。

安装 Flask-WTF
```

pip install flask-wtf
```

配置 Flask-WTF
app.py 文件代码：

实例
```python
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for form protection

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        return f'Name: {name}, Email: {email}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```
创建模板以支持 Flask-WTF 表单
templates/form.html 文件代码：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form method="post">
        {{ form.hidden_tag() }}
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}
        </div>
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
```

{{ form.hidden_tag() }}：生成隐藏字段，用于保护表单免受 CSRF 攻击。

{{ form.name.label }} 和 {{ form.name(size=32) }}：渲染表单字段及其标签。

## 3. 表单验证
Flask-WTF 和 WTForms 提供了丰富的表单验证功能。你可以使用内置的验证器或自定义验证器来确保表单数据的有效性。

实例
```python
from wtforms import Form, StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=1, max=50)
    ])
    email = EmailField('Email', validators=[
        DataRequired(), Email()
    ])
    submit = SubmitField('Submit')
```

DataRequired()：确保字段不为空。
Length(min=1, max=50)：限制字符串的最小和最大长度。
Email()：验证字段是否为有效的电子邮件地址。
## 4. 文件上传
Flask 还支持处理文件上传。上传的文件可以通过 request.files 访问。

创建文件上传表单
templates/upload.html 文件代码：

实例
```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="file">File:</label>
        <input type="file" id="file" name="file">
        <br>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

enctype="multipart/form-data"：指定表单数据的编码类型，支持文件上传。

处理文件上传
app.py 文件代码：

实例
```python
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        filename = file.filename
        file.save(f'uploads/{filename}')
        return f'File uploaded successfully: {filename}'
    return 'No file uploaded'

if __name__ == '__main__':
    app.run(debug=True)
request.files.get('file')：获取上传的文件对象。
```
file.save(f'uploads/{filename}')：将文件保存到指定目录。

## 5. CSRF 保护
Flask-WTF 自动为表单提供 CSRF 保护。你需要配置一个密钥来启用 CSRF 保护，并在模板中包含隐藏的 CSRF 令牌。

配置 CSRF 保护
app.secret_key = 'your_secret_key'
在模板中添加 CSRF 令牌：

实例
```html
<form method="post">
    {{ form.hidden_tag() }}
    <!-- Form fields here -->
</form>
```
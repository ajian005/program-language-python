## Flask 安装
Flask 安装还是比较简单的。

Flask 是 Python的一个库，所以首先需要确保你的计算机上已经安装了 Python。

Flask 需要 Python 3.6 及以上版本，先确保你已安装 Python 3。

可以通过以下命令检查 Python 版本：
```
python --version
```
或者，如果你使用 python3 命令：
```
python3 --version
```
### 使用 pip 安装 Flask
我们可以使用 Python 的包管理器 pip 可以用来安装Flask。

打开你的命令行工具（在 Windows 上是命令提示符或 PowerShell，在 macOS 或 Linux 上是终端），然后运行以下命令：
```
pip install Flask
```
安装完成后，可以通过以下命令验证 Flask 是否安装成功：
```
pip show Flask
```
执行以上命令，显示结果类似如下：
```
Name: Flask
Version: 3.0.3
Summary: A simple framework for building complex web applications.
Home-page: 
Author: 
Author-email: 
License: 
Location: /Users/RUNOOB/.pyenv/versions/3.9.7/lib/python3.9/site-packages
Requires: itsdangerous, Jinja2, blinker, Werkzeug, click, importlib-metadata
Required-by: 
```
这样我们就成功安装了 Flask 包。
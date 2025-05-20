
from flask import Flask, request

app = Flask(__name__)


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
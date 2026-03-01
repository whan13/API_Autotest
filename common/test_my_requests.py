import pytest
from common.method import MyRequests

@pytest.fixture
def api():
    """初始化接口对象"""
    return MyRequests(base_url="https://jsonplaceholder.typicode.com")

def test_get_post_list(api):
    """测试 GET 请求：获取列表"""
    response = api.get("/posts")
    assert response is not None
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_single_post(api):
    """测试 GET 请求：获取单条数据"""
    response = api.get("/posts/1")
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data

def test_post_create(api):
    """测试 POST 请求：创建数据"""
    payload = {"title": "Hello", "body": "World", "userId": 1}
    response = api.post("/posts", json=payload)
    assert response.status_code == 201
    assert response.json()['title'] == "Hello"

def test_404_error(api):
    """测试异常处理：请求不存在的路径"""
    # 访问一个不存在的 ID，JSONPlaceholder 404 会触发 raise_for_status
    response = api.get("/invalid_path/999999")
    assert response is None  # 因为你的代码在 except 里返回了 None
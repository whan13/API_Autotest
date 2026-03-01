import pytest
import time

@pytest.fixture(scope="session", autouse=True)
def global_timer():
    """
    这是一个全局计时器示例
    scope="session" 表示整个测试过程中只执行一次
    """
    print(f"\n[🚀] 测试开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    yield
    print(f"\n[🏁] 测试结束时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

@pytest.fixture(scope="function")
def login_token():
    """
    模拟登录获取 Token 的固件
    你可以在测试函数中直接调用它
    """
    print("\n[🔑] 正在模拟登录获取 Token...")
    token = "mock_token_123456"
    return token
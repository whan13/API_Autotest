import logging, time, os
from common.public_path import read_path
class Logger:
    def __init__(self):
        # 获取当前系统日期，格式为：2026_02_27
        now_time=time.strftime('%Y_%m_%d')
        # 拼接日志文件的完整路径，例如：/项目根目录/log/2026_02_27.log
        self.log=read_path('log',f'{now_time}.log')
        # print(self.log)#调试用
        # 定义日志的显示格式：时间 - 日志级别 : 消息内容
        self.stdout_format = '%(asctime)s - %(levelname)s : %(message)s'

        # log_name = time.strftime('%Y-%m-%d', time.localtime()) + '.log'
        # check_folder_exists = lambda folder: os.path.exists(folder)
        # if not check_folder_exists(log_folder):
        #     os.makedirs(name=log_folder, exist_ok=True)
        # self.stdout_format = '%(asctime)s - %(levelname)s : %(message)s'
        # self.log = os.path.abspath(os.path.join(log_folder, log_name))

    def logger(self):
        #设置日志输出格式  创建一个格式化器，应用上面定义的显示格式
        formatter = logging.Formatter(self.stdout_format)
        #设置控制台日志   让日志显示在 PyCharm 的运行窗口里
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        #设置文件日志  让日志保存到本地 .log 文件中，指定 utf-8 防止中文乱码
        file_handler = logging.FileHandler(filename=self.log, encoding='utf-8')
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)
        # 获取日志对象，并把上面两个处理器（控制台和文件）添加进去
        logging.getLogger().addHandler(console)
        logging.getLogger().addHandler(file_handler)
        # 设置日志收集级别为 INFO（记录常规信息及以上级别的日志）
        logging.getLogger().setLevel("INFO")
        return logging.getLogger()
    
# 实例化 Logger 并调用 logger() 方法，得到一个全局可用的 log 对象
log = Logger().logger()

def trace_log(func):
    """
    这是一个日志装饰器，用来自动记录函数的执行情况
    """
    def wrapper(*args, **kwargs):
        # 在函数执行前：记录函数名、位置参数(*args)和关键字参数(**kwargs)
        log.info('Function:[{}], args:{}, kwargs:{}'.format(func.__name__, args, kwargs))
        # 正式执行被装饰的函数（如 test_login）
        result = func(*args, **kwargs)
        # 在函数执行后：记录函数名和它的返回值（Result）
        log.info('Function:[{}], Result: {}'.format(func.__name__, result))
        # 返回函数的执行结果，保证原函数功能不受影响
        return result
    return wrapper


if __name__ =='__main__':
    """调试代码"""
    @trace_log
    def add(a, b):
        return a+b
    add(1, 2)



"""
装饰器Decorator 本质上是一个“包装纸”。它的作用是：在不修改原函数代码的前提下，给函数增加额外的功能。

装饰器是怎么工作的？
当你给一个函数加上 @trace_log 时，相当于执行了以下逻辑：

拦截：程序在调用该函数前，先跳进装饰器里。

加工：装饰器先执行一些操作（比如你的代码里是打印 log.info 记录入参）。

放行: 装饰器内部执行原函数result = func(...)

收尾：函数执行完后，装饰器再做点别的事（记录出参），最后把结果还给调用者。
"""
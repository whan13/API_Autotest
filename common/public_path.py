## 获取文件的绝对路径

import os  

# os.path.abspath(__file__)：获取当前运行的这个 .py 文件的“绝对路径”（包含文件名）
# os.path.dirname(...)：去掉文件名，只保留文件夹部分
# 打印当前文件所在的文件夹路径
print(os.path.dirname(os.path.abspath(__file__))) 

# __file__ 是当前文件的内置变量
# 第一次 dirname 获取当前文件夹，第二次 dirname 获取它的上一层（父级）文件夹
# base_path 通常被当作“项目根目录”，方便后续以此为基准找其他文件
base_path = os.path.dirname(os.path.dirname(__file__)) 

# 定义一个函数，用来拼接最终的文件路径
# filedir='data' 是默认参数，如果你不传文件夹名，它就默认找名为 data 的文件夹
# filename=None 是文件名占位
def read_path(filedir='data', filename=None):
    # os.path.join 会根据你的操作系统（Windows用\，Mac/Linux用/）自动用斜杠拼接路径
    # 结果类似于：项目根目录/data/Data.xlsx
    return os.path.join(base_path, filedir, filename)

# 这是程序的入口点。只有直接运行这个脚本时，下面的代码才会执行
# 如果这个文件被当做模块导入到别的文件，下面这两行就不会跑
if __name__ == '__main__':
    # 调用函数，传入文件夹 'data' 和文件名 'Data.xlsx'，并打印出拼接后的完整绝对路径
    print(read_path('data', 'Data.xlsx'))
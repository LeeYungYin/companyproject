"""配置

yaml,通用配置格式，python，java，php，GO
py,在python项目中读取更方便
"""

#隐式等待时间
import os

IMPLICTLY_WAIT_TIMEOUT = 20
HOST = "http://192.168.1.222:22101/"

# root path
ROOT_PATH =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# excel_path
EXCEL_PATH = os.path.join(ROOT_PATH, 'data')

# image_path
IMG_PATH = os.path.join(ROOT_PATH, "screenshot")


# totindex/__init__.py
__version__ = "1.0.3"  # 版本号，保持与 setup.py 中一致

from .main import App, main
import os

def get_data_file():
    """
    返回 TOT实验数据.xlsx 的完整路径
    """
    return os.path.join(os.path.dirname(__file__), "data", "TOT实验数据.xlsx")


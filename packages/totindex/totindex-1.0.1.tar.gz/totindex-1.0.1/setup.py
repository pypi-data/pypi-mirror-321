from setuptools import setup, find_packages
setup(
    name="totindex",
    version="1.0.1",
    description="A sample Python package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zhang Zuo Hou Wenjiao Liu Xiaoge",
    author_email="zhangzuocug@163.com",
    url="https://github.com/zhangzuocughustccnu/Topics-Objectives-Tools-Index-Model-TOT-Index-Model",
    packages=find_packages(),  # 自动发现所有 Python 包
    include_package_data=True,  # 包含额外的非代码文件
    install_requires=[
        # 添加你的依赖包，例如:
        # "numpy>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "totindex=totindex.main:main",  # 命令行入口
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

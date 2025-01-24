from setuptools import setup, find_packages
setup(
    name="totindex",
    version="1.0.3",
    description="TOT指数衡量了政策文本在主题全局性、目标贯通性和工具多样性三方面的表现。较高的得分表明该政策文本在内容设计上更具全面性、协调性和丰富性；较低的得分反映了政策文本可能聚焦于特定目标或优先事项，但并不意味着政策本身存在缺陷，而是文本内容设计的取向不同。政策主题X反映了主题格局的全局性水平，得分越高表示政策对于核心主题的涵盖更加完整、全局性水平更高，反之，则更聚焦于局部核心主题。政策目标Y反映了目标优序的贯通程度，得分越高表明数量、质量、生态三个目标递进更深入、贯通性更强；反之，则表明目标贯通性相对不足。政策工具Z反映了工具结构的多样化程度，得分越高表示工具组合更具多样性；反之，则表示相对单一。TOT指数的计算原理基于模糊集赋值原则，旨在科学、合理地量化政策文本内容",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zhang Zuo Hou Wenjiao Liu Xiaoge",
    author_email="zhangzuocug@163.com",
    url="https://github.com/zhangzuocughustccnu/Topics-Objectives-Tools-Index-Model-TOT-Index-Model",
    packages=find_packages(),  # 自动发现所有 Python 包
    include_package_data=True,  # 包含额外的非代码文件
    package_data={
        "totindex": ["data/TOT_Experimental_Data.xlsx"],  # 确保文件路径正确
    },
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

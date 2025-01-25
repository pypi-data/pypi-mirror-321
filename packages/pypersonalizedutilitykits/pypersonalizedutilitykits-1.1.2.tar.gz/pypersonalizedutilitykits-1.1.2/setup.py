# -*- coding:utf-8 -*-
"""
@Time        : 2025/1/16 15:45
@File        : setup.py
@Author      : lyz
@Version     : python 3.11
@Description : 
"""
from setuptools import setup, find_packages

"""
查找项目中的包
"""
packages = find_packages()
print(f"Found packages: {packages}")

"""
读取 README.md 文件
"""
with open('PyUtilToolKit/README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
print(f"Long description:\n{long_description}")

setup(
    name='pypersonalizedutilitykits',
    version='1.1.2',
    description='Python Personalized Kits',
    author='Great people',
    author_email='',
    long_description=long_description,
    # url='https://github.com/your_username/my_package',  # 项目的 GitLab 地址或其他主页
    packages=packages,
    keywords='kit',
    install_requires=[
        'colorlog==6.8.2',
    ],
    license="GPLv3",  # 开源协议
    # 这 需要去官网查，在下边提供了许可证连接 或者 你可以直接把我的粘贴走
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"],
    python_requires='>=3.10',
)

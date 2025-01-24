# -*- coding:utf-8 -*-
"""
@Time        : 2025/1/16 15:45
@File        : setup.py
@Author      : lyz
@Version     : python 3.11
@Description : 
"""
from setuptools import setup, find_packages

setup(
    name='pypersonalizedutilitykits',
    version='1.0.4',
    description='This is my amazing package',
    author='FranklinLiu',
    author_email='3517005858@qq.com',
    # url='https://github.com/your_username/my_package',  # 项目的 GitHub 地址或其他主页
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10',
)
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
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
print(f"Long description:\n{long_description}")

setup(
    name='personalizedutilitykits',
    version='1.0.4',
    description='Python Personalized Kits',
    author='FranklinLiu',
    author_email='3517005858@qq.com',
    long_description=long_description,
    # url='https://github.com/your_username/my_package',  # 项目的 GitLab 地址或其他主页
    packages=packages,
    keywords='kit',
    install_requires=[
        'colorlog==6.8.2',
    ],
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

from setuptools import setup, find_packages

setup(
    name='bioDP',
    version='0.1.3',
    description='pi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='bit15k',
    author_email='i@logdict.com',
    url='https://github.com/bit15k/bioDP',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        # 其他依赖项
    ],
    entry_points={
        'console_scripts': [
            'bioDP-metabodirect=bloDP.metabodirect.cli:main',  # 假设 cli.py 中有一个 main 函数作为命令行入口
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'

    ],
)
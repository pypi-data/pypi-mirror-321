from setuptools import setup, find_packages

setup(
    name='bioDP',
    version='0.1.1',
    description='A package for biological data processing, especially related to metabodirect',
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
            'bioDP-metabodirect=metabodirect.cli:main',  # 假设 cli.py 中有一个 main 函数作为命令行入口
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
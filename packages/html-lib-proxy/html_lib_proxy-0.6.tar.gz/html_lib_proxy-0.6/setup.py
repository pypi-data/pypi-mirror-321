from setuptools import setup, find_packages

setup(
    name='html_lib_proxy',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    py_modules=["utils_proxy"],  # 指定单模块文件
    author="tenc123",
    author_email="myz50w@gmail.com",
    description="test",
)

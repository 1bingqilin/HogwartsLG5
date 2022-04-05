from setuptools import setup

setup(
    name="pytest_encode",
    url="https://github.com/xxx/pytest_encode",
    version="1.0.1",
    author="xixi",
    author_email="418974188@qq.com",
    description="set your encoding and logger",
    long_description='Show Chinese for your mark.parametrize() ',
    classifiers=[#分类索引 pip对所属包的分类
        "Framework :: Pytest",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development  :: Testing",
    ],
    license = 'proprietary',
    packages=['pytest_encode'],
    keywords = [
        'pytest','py.test','pytest_encode'
    ],
    #需要安装的依赖
    install_requires =[
        'pytest'
    ],
    #入口模块  或入口函数
    entry_points = {
        #pytest11是关键字
        'pytest11': [
            'pytest_encode = pytest_encode'
        ]
    },

    #Windows操作系统必须加的，不然报错
    zip_safe = False
)
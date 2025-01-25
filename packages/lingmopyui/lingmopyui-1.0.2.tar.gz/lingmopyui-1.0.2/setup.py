import setuptools  # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lingmopyui",  
    version="1.0.2", 
    author="Admibrill",  
    author_email="admibrill@outlook.com", 
    description="A Lingmo GUI Library based on PySide6.QtWidgets",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/LingmoOS/LingmoPyUI",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts" : ['mwjApiTest = mwjApiTest.manage:run']
    }, #安装成功后，在命令行输入mwjApiTest 就相当于执行了mwjApiTest.manage.py中的run了
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license='GPLv3',
    python_requires='>=3.6',  # 对python的最低版本要求
)
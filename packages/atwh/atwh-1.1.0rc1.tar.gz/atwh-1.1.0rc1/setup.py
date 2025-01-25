from setuptools import setup, find_packages

setup(
    name="atwh",  # 包的名称
    version="1.1.0-rc1",  # 版本号
    description="AnythingWarehouse",  # 简短描述
    long_description=open("readme.md").read(),  # 长描述
    long_description_content_type="text/markdown",  # 描述格式
    author="PaddyHong",
    author_email="1707262291@qq.com",  # 邮箱
    license="gpl",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=(
        "tuitools",
    ),
)

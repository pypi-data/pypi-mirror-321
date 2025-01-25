from setuptools import setup, find_packages

setup(
    name="aloha-flask-creator",  # 修改为你想要的包名
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "aloha-flask-creator = project_creator.create_project:main",  # 修改为新的命令名
        ],
    },
)

import os
import requests
import zipfile

def create_project(project_name):
    # 设定 GitHub API URL 和模板仓库的路径
    repo_url = "https://github.com/TheadoreL/flask-vue-template"
    clone_url = f"{repo_url}/archive/main.zip"

    # 使用 requests 获取仓库的 zip 文件
    response = requests.get(clone_url)

    # 保存为 zip 文件
    with open(f"{project_name}.zip", "wb") as f:
        f.write(response.content)

    # 解压文件
    with zipfile.ZipFile(f"{project_name}.zip", 'r') as zip_ref:
        zip_ref.extractall(project_name)

    # 删除 zip 文件
    os.remove(f"{project_name}.zip")

    print(f"New project created at: {project_name}")

def main():
    # 提示用户输入项目名称
    project_name = input("Please enter the name of the new project: ")

    # 调用 create_project 函数来创建项目
    create_project(project_name)

if __name__ == "__main__":
    main()

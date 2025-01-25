import os
import requests
import zipfile
import shutil

def create_project(project_name):
    # 设定 GitHub API URL 和模板仓库的路径
    repo_url = "https://github.com/TheadoreL/flask-vue-template"
    clone_url = f"{repo_url}/archive/master.zip"

    # 使用 requests 获取仓库的 zip 文件
    response = requests.get(clone_url)

    # 保存为 zip 文件
    zip_file = f"{project_name}.zip"
    with open(zip_file, "wb") as f:
        f.write(response.content)

    # 解压文件
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # 获取解压后的文件夹名（例如 flask-vue-template-master）
        extracted_folder_name = zip_ref.namelist()[0].split("/")[0]  # 获取第一层文件夹名
        zip_ref.extractall()

    # 重命名解压后的文件夹为 project_name
    os.rename(extracted_folder_name, project_name)

    # 删除 zip 文件
    os.remove(zip_file)

    print(f"New project created at: {project_name}")

def main():
    # 提示用户输入项目名称
    project_name = input("Please enter the name of the new project: ")

    # 调用 create_project 函数来创建项目
    create_project(project_name)

if __name__ == "__main__":
    main()

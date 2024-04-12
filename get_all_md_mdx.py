import os
import shutil

# 定义原始文件夹路径和目标文件夹路径
source_folder = './'  # 更改为你的源文件夹路径
target_folder = 'all_doc'  # 新建的目标文件夹路径

# 创建目标文件夹
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.md') or file.endswith('.mdx'):
            # 构建原始文件路径和目标文件路径
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_folder, os.path.splitext(file)[0] + '.txt')
            # 复制并重命名文件
            shutil.copy(source_file_path, target_file_path)
            print(f"File {file} copied and renamed to {os.path.basename(target_file_path)}")

print("All .md and .mdx files copied and renamed to .txt in 'all_doc' folder.")

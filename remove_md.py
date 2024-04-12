
import os
import markdown2
import mistune
import re

# def extract_plain_text_with_markdown2(markdown_text):
#     html = markdown2.markdown(markdown_text, extras=["no-html"])
#     return re.sub(r'<[^>]+>', '', html).strip()

def extract_plain_text_with_markdown2(markdown_text):
    html = markdown2.markdown(markdown_text, extras=["no-html"])
    plain_text = re.sub(r'<[^>]+>', '', html).strip()  # 去除HTML标签
    plain_text = re.sub(r'\bsidebar_position\b.*\n', '', plain_text)  # 去除含有'sidebar_position'的行
    plain_text = re.sub(r':::', '', plain_text)  # 去除:::
    plain_text = re.sub(r'```' ,'', plain_text)  # 去除```
    # plain_text = re.sub(r'```.*?```', '', plain_text, flags=re.DOTALL)  # 去除含有```的部分


    return plain_text

def extract_plain_text_with_mistune(markdown_text):
    return mistune.markdown(markdown_text)


source_folder = 'all_doc'  # 文件夹A的路径
target_folder1 = 'all_doc_without_md_markdown2_'  # 文件夹B的路径
target_folder2 = 'all_doc_without_md_mistune_'  # 文件夹B的路径


# 创建目标文件夹
if not os.path.exists(target_folder1):
    os.makedirs(target_folder1)
# 创建目标文件夹
if not os.path.exists(target_folder2):
    os.makedirs(target_folder2)

# 遍历文件夹A
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.txt'):
            # 构建原始文件路径和目标文件路径
            source_file_path = os.path.join(root, file)
            target_file_path_markdown2 = os.path.join(target_folder1,  file)
            target_file_path_mistune = os.path.join(target_folder2, file)

            # 读取Markdown文件
            with open(source_file_path, 'r', encoding='utf-8') as file:
                markdown_text = file.read()

            # 提取文本并保存为新文件
            plain_text_markdown2 = extract_plain_text_with_markdown2(markdown_text)
            plain_text_mistune = extract_plain_text_with_mistune(markdown_text)

            # 保存为新文件（使用markdown2）
            with open(target_file_path_markdown2, 'w', encoding='utf-8') as output_file:
                output_file.write(plain_text_markdown2)

            # 保存为新文件（使用mistune）
            with open(target_file_path_mistune, 'w', encoding='utf-8') as output_file:
                output_file.write(plain_text_mistune)

            print(f"File {file} processed and saved to {target_folder1,target_folder2}")

print("All Markdown files processed and saved to 'folder_B'.")

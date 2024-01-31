import os
import json
from app import parse_assembly_to_json

def custom_encoder(obj):
    if isinstance(obj, str):
        return obj.replace('\n', '\\n').replace('\\', '')
    return obj

def process_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        # 在这里进行您的处理逻辑，读取文件内容并进行相应处理
        processed_content = input_file.read()
        output_str = parse_assembly_to_json(processed_content)

    # 在这里进行对处理后的内容的输出操作
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(output_str)
        # json.dump(
        #   output_str,
        #   output_file,
        #   indent=2,
        #   ensure_ascii=False
        # )

def process_folder(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder,  f"{os.path.splitext(filename)[0]}.json")

        # 检查是否是文件
        if os.path.isfile(input_path):
            process_file(input_path, output_path)

# 输入文件夹路径和输出文件夹路径
input_folder_path = './input'
output_folder_path = './output'

# 处理文件夹中的文件
process_folder(input_folder_path, output_folder_path)

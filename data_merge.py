# -*- coding: utf-8 -*-
import os


def merge_txt_files(folder_path, output_file, file_name):
    merged_data = ''

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == file_name:
                surce_file_path = os.path.join(root, file)
                # surce_file_name = os.path.splitext(file)[0]
                with open(surce_file_path, 'r', encoding='utf-8', errors='surrogateescape') as f:
                    merged_data += f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        cleaned_content = merged_data.encode('utf-8', 'surrogateescape').decode('utf-8', 'replace')
        f.write(cleaned_content)

    print("合并完成！")


if __name__ == '__main__':
    folder_path = 'D:/个人文件/data/Classical-Modern-main/Classical-Modern-main/双语数据'  # 替换为包含要合并的txt文件的文件夹路径
    # output_file = 'D:/Individual_event/onmt/target.txt'  # 替换为输出文件的路径和名称

    for file_name, output_file in ['source.txt', './source.txt'], \
                                  ['target.txt', './target.txt']:
        merge_txt_files(folder_path, output_file, file_name)

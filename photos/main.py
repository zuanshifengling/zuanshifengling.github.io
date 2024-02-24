# -*- coding: utf-8 -*-
import os

def add_prefix_to_images(directory, prefix):
    # 检查输入的目录是否存在
    if not os.path.isdir(directory):
        print("提供的路径不是有效的目录。")
        return

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否是图片
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            # 构建新的文件名
            new_filename = prefix + filename
            # 写入新的文件名和格式到标准输出
            print(f"![]({new_filename})")
            # 如果需要，也可以将新的文件名重定向到文件中
            # with open('output.md', 'a') as file:
            #     file.write(f"![]({new_filename})\n")

# 使用示例：假设我们要处理的是'images'文件夹，并添加前缀'new_'
add_prefix_to_images('./imgs/', 'https://zuanshifengling-github-io.pages.dev/photos/imgs/')

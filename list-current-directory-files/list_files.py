# copyright (c) 2022 amit-curiosity
import os

# get current file's path
path = os.path.realpath(__file__)

# get current_file's directory
dir_name = os.path.dirname(path)

# print(os.listdir(dir_name))

# go through directory's files & folders
for file_name in os.listdir(dir_name):
    file, ext = os.path.splitext(file_name)

    # print files with python extension
    if ext == '.py':
        print(file_name)

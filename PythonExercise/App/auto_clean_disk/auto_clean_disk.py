# coding: utf-8
import os
import shutil

# 指定需要删除的文件后缀
del_extension_file = ['.tmp', '._mp', '.log', '.gid', '.chk', '.old', '.xlk', '.bak']
# 指定需要删除的目录名字
del_temp_dir = ['cookies', 'recent', 'Temporary Internet Files', 'Temp','prefetch', 'temp']

# 获取系统盘路径
root_sys_drive = os.environ['systemdrive'] + '\\'
# print(root_sys_drive)

def delete_file_or_dir(path):
    try:
        if os.path.isfile(path):
            # 删除文件
            # os.remove(path)
            print('file: ' + path + ' removed')
        elif os.path.isdir(path):
            # 删除文件夹
            # shutil.rmtree(path)
            print('directory: ' + path + ' removed')
    except WindowsError:
        print('failure: ' + path + " can't remove")


def main():
    # 遍历指定目录底下的所有文件，目录
    for roots, dirs, files in os.walk(root_sys_drive):
        # 遍历所有文件
        for find_file in files:
            # 获取文件扩展名
            file_extension = os.path.splitext(find_file)[1]
            # 检查文件后缀是否与指定的相匹配
            if file_extension in del_extension_file:
                # 组合文件完整路径
                complete_path = os.path.join(roots,find_file)
                # 删除文件
                delete_file_or_dir(complete_path)
        # 遍历所有目录
        for find_dir in dirs:
            if find_dir in del_temp_dir :
                # 组合目录名字
                complete_path = os.path.join(roots, find_dir)
                # 删除文件
                delete_file_or_dir(complete_path)


if __name__ == '__main__':
    main()
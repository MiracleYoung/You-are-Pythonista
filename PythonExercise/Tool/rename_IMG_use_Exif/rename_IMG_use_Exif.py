import os
import exifread

def opExif(file_path, file_name):
    old_full_name = os.path.join(file_path, file_name) # 拼接出原文件路径
    file_suffix = os.path.splitext(file_name)[1] # 拿到原文件后缀
    with open(old_full_name, "rb") as f: # 读取文件头部的EXIF信息
        tags = exifread.process_file(f)

    Tag = "EXIF DateTimeOriginal" # EXIF信息中拍摄时间的标签
    if Tag in tags:
        file_stem = str(tags[Tag]).replace(':', '').replace(' ', '_') # 处理原始时间格式  
        new_name = file_stem + file_suffix # 新文件名：年月日_时分秒.原后缀名
        num = 1
        while os.path.exists(new_name): # 遇到拍摄时间相同则添加序号做以区分
            new_name = file_stem + '_' + str(num) + file_suffix # 新文件名：年月日_时分秒_序号.原后缀名
            num += 1

        new_full_name = os.path.join(file_path, new_name) # 拼接出新文件路径
        print(f"{old_full_name} >>> {new_full_name}")
        os.rename(old_full_name, new_full_name) # 执行重命名操作
    else:
        print(f"No {Tag} found in: {old_full_name}")


IMGPath = "P:\\Personal\\Python\\"  # 修改要处理的目录
for IMGName in os.listdir(IMGPath): 
    full_name = os.path.join(IMGPath, IMGName)
    if os.path.isfile(full_name):
        opExif(IMGPath, IMGName)

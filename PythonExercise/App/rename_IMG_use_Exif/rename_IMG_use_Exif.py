import os
import exifread

# 定义opExif函数对文件进行一系列的处理操作
def opExif(file_path, file_name):
    # 拼接出原文件路径
    old_full_name = os.path.join(file_path, file_name)
    # 拿到原文件后缀 
    file_suffix = os.path.splitext(file_name)[1] 
    # 打开并读取文件头部的EXIF信息
    with open(old_full_name, "rb") as f:
        tags = exifread.process_file(f)

    # EXIF信息中拍摄时间的标签
    Tag = "EXIF DateTimeOriginal"
    if Tag in tags:
        # 调整原始的时间格式为"年月日_时分秒"
        file_stem = str(tags[Tag]).replace(':', '').replace(' ', '_')   
        # 新文件名：年月日_时分秒.原后缀名
        new_name = file_stem + file_suffix
        num = 1
        # 遇到拍摄时间相同则添加序号做以区分
        while os.path.exists(new_name): 
            # 新文件名：年月日_时分秒_序号.原后缀名
            new_name = file_stem + '_' + str(num) + file_suffix
            num += 1
        
        # 拼接出新文件路径
        new_full_name = os.path.join(file_path, new_name) 
        print(f"{old_full_name} >>> {new_full_name}")
        # 执行重命名操作
        os.rename(old_full_name, new_full_name) 
    else:
        print(f"No {Tag} found in: {old_full_name}")

# 修改要处理的目录
IMGPath = "P:\\Personal\\Python\\"

for IMGName in os.listdir(IMGPath): 
    # 拼接出原文件路径
    full_name = os.path.join(IMGPath, IMGName)
    # 判断是否为文件
    if os.path.isfile(full_name):
        # 调用opExif函数
        opExif(IMGPath, IMGName)

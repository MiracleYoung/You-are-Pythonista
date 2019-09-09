#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/5/31 下午10:15
# @Author  : MiracleYoung
# @File    : tar2zip.py


import tarfile, zipfile, glob, os, time
from io import BytesIO


def getuser():
    # 模拟返回用户名、用户id
    return "Miracle", 666


def getmode(name, data):
    # 返回文件类型，"b" 或 "t"
    # 假设我们现在都是字符
    return "t"


now = time.time()
user = getuser()


def fixup(infile):
    file, ext = os.path.splitext(infile)
    outfile = file + ".tar.gz"
    print(f'outfile: {outfile}')

    zip = zipfile.ZipFile(infile, "r")
    tar = tarfile.open(outfile, "w:gz") # 使用gzip、写 模式打开
    tar.posix = 1

    for name in zip.namelist():
        if name.endswith("/"):
            continue

        data = zip.read(name)
        if getmode(name, data) == "t":
            data = data.decode().replace("\r\n", "\n")

        tarinfo = tarfile.TarInfo()
        tarinfo.name = name
        tarinfo.size = len(data)
        tarinfo.mtime = now
        tarinfo.uname = tarinfo.gname = user[0]
        tarinfo.uid = tarinfo.gid = user[1]
        tar.addfile(tarinfo, BytesIO(data.encode()))

    tar.close()
    zip.close()


if __name__ == '__main__':
    # convert all ZIP files in the current directory
    for file in glob.glob("*.zip"):
        fixup(file)

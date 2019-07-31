# encoding: utf-8

'''
需要安装pdfkit, pip install pdfkit
自行下载并安装wkhtmltopdf-binary， http://wkhtmltopdf.org/
'''

import sys
import subprocess

import pdfkit

# 获得ipynb文件
inputfile = sys.argv[1].replace(" ", "\ ")
# 截取ipynb前面的名字，并保留一份html临时文件
# 这份文件会在转换过程中需要
# 因为我是利用jupyter对于html的支持，使用pdfkit对html文件进行转换
temp_html = inputfile[0:inputfile.rfind('.')] + '.html'
# 转换ipynb文件为html
# 调用了ipython接口
command = 'ipython nbconvert --to html ' + inputfile
# shell端执行command
subprocess.call(command, shell=True)
print('============success===========')
# 拼接一个pdf名字
output_file = inputfile[0:inputfile.rfind('.')] + '.pdf'
# 大杀器出场，pdfkit直接将html转换成pdf
pdfkit.from_file(temp_html, output_file)
# 删除html临时文件
subprocess.call('rm ' + temp_html, shell=True)

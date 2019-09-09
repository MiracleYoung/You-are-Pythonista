#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/25 2:00 PM

__author__ = 'Miracle'

from PIL import Image, ImageDraw, ImageFont

img = Image.open("./img/img.jpeg")
jgz = Image.open("./img/jgz.jpeg")
img.paste(jgz, (63, 46))

# 控制表情的叠加位置
draw = ImageDraw.Draw(img)
# 字体自己随便找一个
font = ImageFont.truetype('./font/simsun.ttc', 24)
draw.text((16, 200), "Python专栏", fill=(0, 0, 0), font=font)

# 控制文字添加位置
img.show()
img.save("生成的表情包.jpg")

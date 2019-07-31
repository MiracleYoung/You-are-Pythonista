# @Time    : 2019/07/01 7:55AM
# @Author  : HGzhao
# @File    : to_wordcloud.py

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba


# 解析背景图片
mask_img = plt.imread('Bulb.jpg')

'''设置词云样式'''
wc = WordCloud(
    # 设置字体  
    font_path='SIMYOU.TTF',
    # 允许最大词汇量
    max_words = 2000,
    # 设置最大号字体大小
    max_font_size = 80,
    # 设置使用的背景图片
    mask = mask_img,
    # 设置输出的图片背景色
    background_color=None, mode="RGBA",
    # 设置有多少种随机生成状态，即有多少种配色方案
    random_state=30)

# 读取文件内容
br = pd.read_csv('barrage.csv', header=None)

# 进行分词，并用空格连起来
text = ''
for line in br[1]:
    text += ' '.join(jieba.cut(line, cut_all=False))

# 生成词云
wc.generate_from_text(text)
#改变字体颜色
img_colors = ImageColorGenerator(mask_img)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 将图片保存到本地
wc.to_file("Garbage_classification.png")
print(f'生成词云成功!')

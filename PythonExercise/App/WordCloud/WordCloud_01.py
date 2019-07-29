import jieba
import wordcloud

# 读取词源文件
with open("govreport.txt", 'rb') as f:
    t = f.read()

# 进行分词
ls = jieba.lcut(t)
# 把分词用空格连起来
txt = ' ' .join(ls)

# 设置词云参数
w = wordcloud.WordCloud(
    # 设置字体 
    font_path = 'SIMYOU.TTF', 
    # 设置输出的图片宽高像素值
    width = 1000, height = 700,
    # 设置输出的图片背景色
    background_color = 'white')

# 生成词云
w.generate(txt)

# 将图片保存到本地
w.to_file('2019GovReport.png')

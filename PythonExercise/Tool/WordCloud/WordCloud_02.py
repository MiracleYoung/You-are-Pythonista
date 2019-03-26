# 分词模块
import jieba
# 画图模块
import matplotlib.pyplot as plt
# 文字云模块
from wordcloud import WordCloud
# 这是一个处理图像的函数，读取背景图片
from scipy.misc import imread

# 词源的文本文件
wf = 'govreport.txt'
# 读取文件内容
word_content = open(wf,'r', encoding='utf-8').read().replace('\n','')
# 设置背景图片
img_file = 'China.jpg'
# 解析背景图片
mask_img = imread(img_file)
# 进行分词
word_cut = jieba.cut(word_content)
# 把分词用空格连起来
word_cut_join = " ".join(word_cut)
# 设置词云参数
wc = WordCloud(
    # 设置字体  
    font_path='msyh.ttc',
    # 允许最大词汇量
    max_words = 2000,
    # 设置最大号字体大小
    max_font_size = 90,
    # 设置使用的背景图片，这个参数不为空时，width和height会被忽略
    mask = mask_img,
    # 设置输出的图片背景色
    background_color = 'white')

# 生成词云
wc.generate(word_cut_join)

# 用于显示图片，需配合plt.show()一起使用
plt.imshow(wc)
# 去掉坐标轴
plt.axis('off')
# 将图片保存到本地
plt.savefig('2019GovReport.jpg')
plt.show()
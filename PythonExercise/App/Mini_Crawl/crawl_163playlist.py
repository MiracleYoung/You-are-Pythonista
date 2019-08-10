from selenium import webdriver

# 网易云音乐歌单列表第一页地址
url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# 用Chrome接口创建一个Selenium的WebDriver
browser = webdriver.Chrome()

# 逐页解析，直至歌单列表的最后一页
while url != 'javascript:void(0)':
    # 用WebDriver加载页面
    browser.get(url)
    # 切换至内容的iframe
    browser.switch_to.frame("contentFrame")
    # 定位歌单标签
    data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    # 解析当前页中所有的歌单详情
    for i in range(len(data)):
        # 获取歌单的播放量
        num = data[i].find_element_by_class_name("nb").text
        if '万' in num and int(num.split('万')[0]) > 1000:
            # 获取播放量大于1000万的歌单封面
            msk = data[i].find_element_by_css_selector("a.msk")
            # 把歌单封面中的标题、链接以及播放量，存储在TXT文件中
            with open("163playlist.txt", 'a', encoding='utf-8') as f:
                f.write(' '.join([msk.get_attribute('title'), num, msk.get_attribute("href")]) + '\n' + '=' * 50 + '\n')
    # 定位'下一页'的URL
    url = browser.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href") 
    
# 结束调用
browser.close()

from fontTools.ttLib import TTFont
import requests
import re
import json
from urllib.request import urlretrieve

def get_page(font_names_map=None,font_cmap=None):
    # 首先分析网页，找到返回评论数据的url，这个url就会直接返回评论数据了，但是urlt中的token是会变化的，只能用一会儿，我也不知道一会儿是好久,得不到数据了就换url吧
    url = 'http://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=131013635&cityId=1604&shopType=10&tcv=txgmn7z01d&_token=eJxVj81ugkAUhd9ltp3A%2FCskXag1DQq2MmBSTReAOhIEEYg6Nn33Do1ddHXO%2Fe45yb1foPG2wMUIIYYhuOwa4AJsIUsACLrWbLjgRGBHcIdzCLJ%2FTPABhSBtVi%2FA3TCC4ICzzx6EZt5gTgUcCkMelhhLGCS%2FGc9EwKHrate2r9ertc2Tqs4rZWWn0m4Pp9rGFCNMBeXmFGAqZdRXCKOQDFgPih4YTR7a%2Fc2BecKU2lxVxu1mt0i2rD3vw6CNYhTcx6HWzlxKov0M%2BzKm%2Fn3aLWJ5edOT4UiHRfp6UEl5K1OlVpO56mS6RAvs1X5GgyjXjTOtFlGRyng226%2BPR1nwp2S9uhUfda7Go3d99jz0DL5%2FANI8Y5M%3D&uuid=c59d33fd-e043-a0f5-f6e1-79ae90d14254.1565007755&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2F131013635'

    # 定义模拟请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': 'cy=8; cye=chengdu; _lxsdk_cuid=16c61bb35536e-0e2ab00cb9c2a8-c343162-144000-16c61bb35547b; _lxsdk=16c61bb35536e-0e2ab00cb9c2a8-c343162-144000-16c61bb35547b; _hc.v=c59d33fd-e043-a0f5-f6e1-79ae90d14254.1565007755; s_ViewType=10; __utmz=1.1565010551.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __utma=1.1978331348.1565010551.1565010551.1565161172.2; _lxsdk_s=16c70ded480-ab0-fe2-71%7C%7C2',
        'Referer':'http://www.dianping.com/shop/131013635',
        'Connection': 'keep-alive',
    }

    # 使用requests库请求url，得到数据json数据
    result_json_str = requests.get(url,headers=headers).text
    # 应为返回的数据是富文本数据，所以首先我们先去掉标签
    result_json_str = re.sub('<.*?>','',result_json_str)

    # 遍历 字体代码->字体名字 这个字典（code 是一个数字）
    for code, name in font_cmap.items():
        try:
            # 尝试从 字体名字 -> 对应值 这个字典中得到值，防止程序出现KeyError的错误
            text = font_names_map[name]
        except:
            pass
        else:
            # 分析网页信息得知，将code变成16进制，并且把最前面的0换成&#，在加上一个';'. 就是网页加密了的字符窜了
            code_str = str(hex(code)).replace('0', '&#', 1) + ';'
            print(code, code_str, name, text)
            # 将得到的加密之后的字符串进行替换为相应的数据
            result_json_str = re.sub(code_str, text, result_json_str)

    # 处理之后的数据使用json模块变成字典
    result = json.loads(result_json_str)
    # 分析得到的数据，得到我们需要的所有评论在result['reviewAllDOList']里面
    try:
        all_review = result['reviewAllDOList']
    except:
        print(result_json_str)
        raise ValueError('爬取数据失败')

    # 遍历得到的所有评论
    for review in all_review:
        # 得到用户名
        username = review['user']['userNickName']
        # 得到评论内容
        content = review['reviewDataVO']['reviewBody']
        # 这里我们就是简单的显示出内容就是了，没有进行储存
        print('*'*30,'\n',username,":",content,'\n','*'*30)

def get_font_map():


    # 这个字体文件需要先析网页，找到这个url，然后下载下来到本地，然后使用TTFont()加载字体文件
    font = TTFont('font.woff')
    # 得到cmap 字体对应代码->字体名字
    font_cmap = font.getBestCmap()
    # 得到所有的字体名字
    font_names = font.getGlyphOrder()
    # 这个文字是先使用fontCreator软件打开字体文件，然后查看到字体，从而得到的数据
    texts = [
        '','','1','2','3','4','5','6','7','8',
        '9','0','店','中','美','家','馆','小','车','大',
        '市','公','酒','行','国','品','发','电','金','心',
        '业','商','司','超','生','装','园','场','食','有',
        '新','限','天','面','工','服','海','华','水','房',
        '饰','城','乐','汽','香','部','利','子','老','艺',
        '花','专','东','肉','菜','学','福','饭','人','百',
        '餐','茶','务','通','味','所','山','区','门','药',
        '银','农','龙','停','尚','安','广','鑫','一','容',
        '动','南','具','源','兴','鲜','记','时','机','烤',
        '文','康','信','果','阳','理','锅','宝','达','地',
        '儿','衣','特','产','西','批','坊','州','牛','佳',
        '化','五','米','修','爱','北','养','卖','建','材',
        '三','会','鸡','室','红','站','德','王','光','名',
        '丽','油','院','堂','烧','江','社','合','星','货',
        '型','村','自','科','快','便','日','民','营','和',
        '活','童','明','器','烟','育','宾','精','屋','经',
        '居','庄','石','顺','林','尔','县','手','厅','销',
        '用','好','客','火','雅','盛','体','旅','之','鞋',
        '辣','作','粉','包','楼','校','鱼','平','彩','上',
        '吧','保','永','万','物','教','吃','设','医','正',
        '造','丰','健','点','汤','网','庆','技','斯','洗',
        '料','配','汇','木','缘','加','麻','联','卫','川',
        '泰','色','世','方','寓','风','幼','羊','烫','来',
        '高','厂','兰','阿','贝','皮','全','女','拉','成',
        '云','维','贸','道','术','运','都','口','博','河',
        '瑞','宏','京','际','路','祥','青','镇','厨','培',
        '力','惠','连','马','鸿','钢','训','影','甲','助',
        '窗','布','富','牌','头','四','多','妆','吉','苑',
        '沙','恒','隆','春','干','饼','氏','里','二','管',
        '诚','制','售','嘉','长','轩','杂','副','清','计',
        '黄','讯','太','鸭','号','街','交','与','叉','附',
        '近','层','旁','对','巷','栋','环','省','桥','湖',
        '段','乡','厦','府','铺','内','侧','元','购','前',
        '幢','滨','处','向','座','下','県','凤','港','开',
        '关','景','泉','塘','放','昌','线','湾','政','步',
        '宁','解','白','田','町','溪','十','八','古','双',
        '胜','本','单','同','九','迎','第','台','玉','锦',
        '底','后','七','斜','期','武','岭','松','角','纪',
        '朝','峰','六','振','珠','局','岗','洲','横','边',
        '济','井','办','汉','代','临','弄','团','外','塔',
        '杨','铁','浦','字','年','岛','陵','原','梅','进',
        '荣','友','虹','央','桂','沿','事','津','凯','莲',
        '丁','秀','柳','集','紫','旗','张','谷','的','是',
        '不','了','很','还','个','也','这','我','就','在',
        '以','可','到','错','没','去','过','感','次','要',
        '比','觉','看','得','说','常','真','们','但','最',
        '喜','哈','么','别','位','能','较','境','非','为',
        '欢','然','他','挺','着','价','那','意','种','想',
        '出','员','两','推','做','排','实','分','间','甜',
        '度','起','满','给','热','完','格','荐','喝','等',
        '其','再','几','只','现','朋','候','样','直','而',
        '买','于','般','豆','量','选','奶','打','每','评',
        '少','算','又','因','情','找','些','份','置','适',
        '什','蛋','师','气','你','姐','棒','试','总','定',
        '啊','足','级','整','带','虾','如','态','且','尝',
        '主','话','强','当','更','板','知','己','无','酸',
        '让','入','啦','式','笑','赞','片','酱','差','像',
        '提','队','走','嫩','才','刚','午','接','重','串',
        '回','晚','微','周','值','费','性','桌','拍','跟',
        '块','调','糕'
    ]

    font_name_map = {}

    # 得到字体名字和值得映射表
    for index,value in enumerate(texts):
        font_name_map[font_names[index]] = value

    return font_cmap,font_name_map

def get_font_file():
    url = 'https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/c667da25.woff'
    urlretrieve(url,'font.woff')

if __name__ == '__main__':

    # get_font_file()
    font_cmap, font_names_map = get_font_map()
    get_page(font_names_map,font_cmap)

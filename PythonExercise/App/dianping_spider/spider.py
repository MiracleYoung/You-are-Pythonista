import requests
from lxml import etree

start_url = 'http://www.dianping.com/search/keyword/8/10_%E8%81%9A%E9%A4%90/o2'

def build_headers(refer=None):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'refer' : refer,
        'Connection': 'keep - alive',
        'Cookie': '''_lxsdk_cuid=16c61bb35536e-0e2ab00cb9c2a8-c343162-144000-16c61bb35547b;_lxsdk=16c61bb35536e-0e2ab00cb9c2a8-c343162-144000-16c61bb35547b;_hc.v=c59d33fd-e043-a0f5-f6e1-79ae90d14254.1565007755;s_ViewType=10;__utmz=1.1565010551.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);__utma=1.1978331348.1565010551.1565010551.1565161172.2;cy=8;cye=chengdu;_lxsdk_s=16ca7962980-426-955-310%7C%7C352'''
    }
    return headers

def parse_page(url):
    # headers = build_headers()
    #
    # result = requests.get(url,headers=headers).text
    #
    # parse = etree.HTMLParser(encoding='utf-8')
    # html = etree.HTML(result,parser=parse)
    #
    # hrefs = html.xpath(r'//div[@id="shop-all-list"]//div[@class="tit"]/a/@href')

    hrefs = ['http://www.dianping.com/shop/23093707', 'http://www.dianping.com/brands/b23093707', 'http://www.dianping.com/shop/2461336', 'http://www.dianping.com/shop/90085699', 'http://www.dianping.com/shop/13810171', 'http://www.dianping.com/brands/b13810171', 'http://www.dianping.com/shop/58322041', 'http://www.dianping.com/shop/80620237', 'http://www.dianping.com/shop/130946881', 'http://www.dianping.com/brands/b130946881', 'http://www.dianping.com/shop/32704021', 'http://www.dianping.com/brands/b18005322', 'http://www.dianping.com/shop/75141698', 'http://www.dianping.com/brands/b10008473', 'http://www.dianping.com/shop/92384680', 'http://www.dianping.com/shop/47008792', 'http://www.dianping.com/brands/b47008792', 'http://www.dianping.com/shop/67997136', 'http://www.dianping.com/brands/b4087801', 'http://www.dianping.com/shop/111533101', 'http://www.dianping.com/shop/98779037', 'http://www.dianping.com/shop/102025765', 'http://www.dianping.com/brands/b23093707']


    every_page_headers = build_headers(url)
    print(every_page_headers)
    for href in hrefs:
        result = requests.get(href,headers=every_page_headers).text
        with open('test.html','w',encoding='utf-8') as fp:
            fp.write(result)
        break


if __name__ == '__main__':
    parse_page(start_url)
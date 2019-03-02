import requests
import json

def get_City_data():
    '''
    城市代码对应表获取，生成
    '''
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9098'
    # 伪造浏览器登陆
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
    response = requests.request('GET', url, headers=headers)
    html = response.text
    station_data = html.split('=')[1].split('@')
    ret = {}
    # unit :
    # 'zyi|遵义|ZYE|zunyi|zy|2844'
    for unit in station_data:
        if '|' not in unit:
            continue
        ret[unit.split('|')[1]] = unit.split('|')[2]
    return ret

def get_trains_info(date,from_station,to_station):
    '''
    火车信息查询方法函数
    '''
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
    response = requests.request('GET', url, headers=headers)
    html = response.text
    return html

def main(date,startcity,endcity):
    # 获取全国的火车站的名字及代码对应表
    data = get_City_data()
    # 返回火车票接口查询数据
    info = get_trains_info(date,data[startcity],data[endcity])
    # info:
    # {"data":{"flag":"1","map":{"HHC":"呼和浩特","SHH":"上海","SNH":"上海南"},"result":["qdgqdG3D3WtakRGGRveYXv0UT0LC%2By5Uz7Q45v2YXTTFSFD2F1ytJO5zmXQeRQSD7IqTtb3ue2mr%0ATnX9IpMriDEUepM2%2BH2d1J%2BF%2B0EM70zVFVFlX4VhLDnDrwalXkpzTvhho9OioSKh5saXppwe3dPL%0AcSgQRBqtpixVJMwPq8nOT9iRj1Ze%2BzDYkPcDowgWH88EipYmYGFxBaELLY9NQKdKt8oUxy9TJtXI%0AARKxKTtYnDqj3nNCy%2FH6CM92pqdRxaf64KcpGiPX0nzCW3hPaD383mIfL4pok9X1MTjsI4KswOgz%0Az8xgIY%2B5shsAO50gcQYI2v0plxo%3D|预订|550000Z26810|Z268|SHH|HHC|SHH|HHC|14:54|18:10|27:16|Y|IH%2F0kUZSZGaDFtha7xB0ish50Wb1nieax2UHqb9SsTVkrWv9dhmXNOiBNA55JmKUAGXU%2Bbjb39U%3D|20190310|3|H1|01|27|0|0||无||有|||有||有|有|||||1040106030|14163|0|0|null","NNla2x3ih8pkHi7W5Z4QdHda5NT0BGE0ZTQGhfsMg32VdWZHQWK7h%2Bqyk%2BMxQ722akslmioV%2BslX%0AD2P2xXK%2BGfWedMBE2xTfQxiLHf7UirTUDUyvOpZLXt5wiyiROR0YBC4uaFtEHBluxEFYlvFf%2B7hl%0A16eGXI%2FW2AJCcuyIipMzGsZ6HFSAmvwzcdsaruYMQ3fuLRb4jJxPj2hTRMNv0zwEmy1UUrMpwUWV%0AORxv99ff%2Bk6Mc1QPbNnmYZ0w1W87wlGEjKoBEnAhw338lMOySPaveyQ%2B%2BEGKcaHkdfiWq35cqPC6%0AfKPAIqQ8pp5sJMa%2F|预订|560000Z28230|Z282|HZH|BTC|SNH|HHC|19:30|20:32|25:02|Y|ODhqzhoV01dsu9acj9mJ3Lzts24eR4unUZ0Iza%2F2I302E9%2FnR8jqeCwpVww%3D|20190310|3|H6|04|20|0|0||||3|||无||有|有|||||10401030|1413|0|0|null"]},"httpstatus":200,"messages":"","status":true}
    hjson = json.loads(info)["data"]["result"]
    # raw_train:
    # "|预订|550000Z16420|Z164|SHH|LSO|SHH|LSO|20:08|19:30|47:22|N|SIygZtG7LXRkGXyeINjk7T5kNo40ywRzkHSmSiTp6MyIlkHIGPlTcQfsc9U%3D|20190303|3|H2|01|14|0|0||||无|||无||无|无|||||10401030|1413|0|0|null"
    for raw_train in hjson:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')
        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_name = startcity
        # 终点站
        to_station_name = endcity
        # 出发时间
        start_time = data_list[8]
        # 到达时间
        arrive_time = data_list[9]
        # 总耗时
        time_used_up = data_list[10]
        # 一等座
        first_class_seat = data_list[31] or '--'
        # 二等座
        second_class_seat = data_list[30] or '--'
        # 软卧
        soft_sleep = data_list[23] or '--'
        # 硬卧
        hard_sleep = data_list[28] or '--'
        # 硬座
        hard_seat = data_list[29] or '--'
        # 无座
        no_seat = data_list[26] or '--'

        list = ('车次:{} 出发站:{} 目的地:{} 出发时间:{} 到达时间:{} 火车运行时间:{} 座位情况：\n 一等座：「{}」 二等座：「{}」 软卧：「{}」 硬卧：「{}」 硬座：「{}」 无座：「{}」'.format(train_no, from_station_name, to_station_name, start_time, arrive_time, time_used_up, first_class_seat,second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

        print('*'*100)
        print(list)
        print('*'*100)


date = str(input('请输入日期(格式“2019-01-01”)： '))
startcity = str(input('出发站： '))
endcity = str(input('到达站：'))

if __name__ == '__main__':
    try:
        main(date,startcity,endcity)
    except KeyError:
        print('您输入的数据有问题，请重新输入')

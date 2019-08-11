from collections import namedtuple
import time


tmp = []
ret = []
names = ["ip", "", "", "times", "m_r_h", "status", "response_length", "", "UA"]
Logs = namedtuple("Logs", ["ip", "times", "method", "routing", "http_v", "status", "response_length", "UA"])
    
mapping = {
    "ip": lambda x: x,
    "times": lambda x: time.mktime(time.strptime(x[1:-1], "%d/%b/%Y:%H:%M:%S %z")),
    "method": lambda x: x.strip('"').split()[0],
    "routing": lambda x: x.strip('"').split()[1],
    "http_v": lambda x: x.strip('"').split()[2],
    "status": lambda x: int(x),
    "response_length": lambda x: int(x),
    "UA": lambda x: x.strip('"\n'),
}

def extract(data):
    """提取 log

    @params data: A log message
    @return: Logs
    """
    split = True
    for i in data:
        # 按空格来分
        if i == "[":
            split = False
        if i =="]":
            split = True
        
        if i == '"':
            split = not split

        if i == " " and split:
            ret.append("".join(tmp))
            tmp.clear()
        else:
            tmp.append(i)
    else:
        ret.append("".join(tmp))
    
    s_dic = dict(zip(names, ret))

    log = Logs(
        ip=mapping["ip"](s_dic['ip']),
        times=mapping["times"](s_dic['times']),
        method=mapping["method"](s_dic['m_r_h']),
        routing=mapping["routing"](s_dic['m_r_h']),
        http_v=mapping["http_v"](s_dic['m_r_h']),
        status=mapping["status"](s_dic['status']),
        response_length=mapping["response_length"](s_dic['response_length']),
        UA=mapping["UA"](s_dic['UA']),
    )

    return log


if __name__ == "__main__":
    # 打开文件获取第一条 log
    with open("../access.log", "r", encoding="utf-8") as f:
        data = f.readline()

    print(data)
    log = extract(data)
    print(log)
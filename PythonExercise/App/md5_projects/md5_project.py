import hashlib
import hmac

def md5_demo():
    data = '123456'
    # 新建一个md5算法对象
    md5 = hashlib.md5()
    # 对数据进行加密
    md5.update( data.encode('utf-8') )
    # 得到加密之后的值
    print(md5.hexdigest())

def big_data_md5():
    data0 = 'hello world'
    data1 = 'hello '
    data2 = 'world'

    md5_0 = hashlib.md5()
    md5_1 = hashlib.md5()

    md5_0.update(data0.encode('utf-8'))
    md5_1.update(data1.encode('utf-8'))
    md5_1.update(data2.encode('utf-8'))

    print(md5_0.hexdigest())
    print(md5_1.hexdigest())

def sha1_demo():
    data = '123456'

    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    print(sha1.hexdigest())

def add_salt_md5():
    SECRET_KEY = 'asdfghjkl'
    data = '123456'

    md5 = hashlib.md5()

    # 下面两种update方式得到的结果是一样的
    # md5.update( (SECRET_KEY + data).encode('utf-8') )

    md5.update(SECRET_KEY.encode('utf-8'))
    md5.update(data.encode('utf-8'))

    print(md5.hexdigest())

def hamc_dem0():
    data = '123456'.encode('utf-8')
    SECRET_KEY = 'asdfghjkl'.encode('utf-8')

    # 下面两种写法是等价的
    h = hmac.new(key=SECRET_KEY, msg=data, digestmod='md5')

    # h = hmac.new(SECRET_KEY, digestmod='MD5')
    # h.update(data)

    print(h.hexdigest())

def make_md5():
    # source = '1234'
    # b_source = source.encode('utf-8')
    # print(len(b_source))
    print(int('1234567',16))

if __name__ == '__main__':
    make_md5()
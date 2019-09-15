# python hashlib与md5加密原理

### 演示环境
* 操作系统：windows10
* python版本：python 3.7
* 代码编辑器：pycharm 2018.2
* 使用模块：hashlib

### hashlib库简介
python的hashlib库给我们提供了常见的摘要算法，如md5，sha1等等。

什么是摘要算法呢？
摘要算法又叫hash算法，散列算法。通过这个算法，我们可以把`任意长度`的数据转化为一个`长度固定`的数据字符窜。
摘要算法也是一个单向的算法，我们讲一个字符窜进行摘要算法加密之后，我们再想将这个字符窜还原，是非常困难的，而且，字符窜之间只要有一点点的不同，摘要算法加密之后的字符窜也是完全不同的。所以他经常被用来做密码的加密。

### hashlib的使用
1. md5加密
```python
import hashlib

def md5_demo():
    data = '123456'
    # 新建一个md5算法对象
    md5 = hashlib.md5()
    # 对数据进行加密
    md5.update( data.encode('utf-8') )
    # 得到加密之后的值
    print(md5.hexdigest())
```

上面就是md5算法的简单使用，需要注意的是，加密的数据必须是编码之后的数据，所以我们需要先对字符窜进行编码，然后在加密。

如果需要加密的数据很长，那么我们可以多次调用update方法。
```python
import hashlib
def big_data_md5():
    data0 = 'hello world'
    data1 = 'hello '
    data2 = 'world'

    md5_0 = hashlib.md5()
    md5_1 = hashlib.md5()
    
    # 调用一次update
    md5_0.update(data0.encode('utf-8'))
    # 调用多次update
    md5_1.update(data1.encode('utf-8'))
    md5_1.update(data2.encode('utf-8'))

    print(md5_0.hexdigest())
    print(md5_1.hexdigest())
```
这两种方式加密出来的结果都是一样的，所以我们的数据量很大的时候，我们就可以多次update，然后再加密。

md5是最常见的摘要算法，速度很快，生成的结果是福鼎的128bit字节，通常使用32位16进制字符窜表示

2. sha1加密

和md5加密调用方法一样
```python
import hashlib
def sha1_demo():
    data = '123456'

    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    print(sha1.hexdigest())
```

sha1加密的结果是160bit,通常用一个40位的16进制字符窜表示

比sha1更安全的算法还有sha256和sha512加密，不过越安全的算法越慢，而且摘要长度也很长。

那么有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
这是有可能的，但是出现的几率非常非常小。

3. 给摘要算法`"加盐"`
什么是给摘要算法加盐呢？
比如我们在给密码进行摘要算法加密的时候，我们直接只用md5或者sha1等加密算法加密，然后将得到的值存入数据库中。这样看起来是没有问题的。但是如果用户设置的密码过于简单，如`123456`这样的弱密码，假如我们是一名黑客，那么我们是可以事先计算好一些简单的弱密码的MD5值得，就能得到一个反推表，在和我们的数据库进行对比，就能够得到一些弱密码了。

所以，对于用户来说，尽量不要使用简单的弱密码。但是我们能否在程序中对简单口令加强保护呢？
答案当然是可以的，我们可以先设置一窜复杂的字符窜，然后将用户的密码和我们设置的字符窜进行拼接，然后在一起加密，这样，就算用户的密码设置的很简单，但是和我们设置的字符窜拼接之后，也变得不是那么简单了。这就是`"加盐"`.

```python
import hashlib
def add_salt_md5():
    SECRET_KEY = 'asdfghjkl'
    data = '123456'

    md5 = hashlib.md5()
    
    # 下面两种update方式得到的结果是一样的
    # md5.update( (SECRET_KEY + data).encode('utf-8') )
    
    md5.update(SECRET_KEY.encode('utf-8'))
    md5.update(data.encode('utf-8'))
    
    print(md5.hexdigest())
```

熟悉django的朋友应该都知道，在setting文件中，就有一个`SECRET_KEY`这个变量，django就是用这一窜字符进行`加盐`的.

4. hmac算法
上面我们对密码进行了加盐，其实这就是标准的hmac算法，我们来看一下使用hmac怎样进行加密。

```python
import hmac
def hamc_dem0():
    data = '123456'.encode('utf-8')
    SECRET_KEY = 'asdfghjkl'.encode('utf-8')

    # 下面两种写法是等价的
    h = hmac.new(key=SECRET_KEY, msg=data, digestmod='md5')
    
    # h = hmac.new(SECRET_KEY, digestmod='MD5')
    # h.update(data)
    
    print(h.hexdigest())
```

hamc默认是使用的MD5算法，我们也可以改成sha1算法等。

可以看见使用hmac和普通的hash算法非常类似，hmac的输出长度和原始的哈希算法长度一致，需要注意的是传入的key和message都是bytes类型的，str就需要先编码为bytes。


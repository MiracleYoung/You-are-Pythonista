import requests
import json
import getpass

class Login():
    def __init__(self):
        '''
        初始化操作
        '''
        # 模拟浏览器请求头
        self.agent_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }
        # 建立会话对象(接下来的登陆都要依赖这个会话)
        self.session = requests.session()

    def get_authentication_photo(self):
        '''
        下载验证码的图片
        '''
        photo_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
        # 请求验证码url并返回结果
        response = self.session.get(url=photo_url, headers=self.agent_header, verify=False)
        # 将返回结果以二进制写入image.jpg文件
        with open('image.jpg','wb') as f:
            f.write(response.content)
        print('请到脚本执行同路径去看image.jpg这个文件')

    def Check_Authentication_Code(self):
        '''
        验证码验证接口
        '''
        # 8张图的中间位置坐标
        view_location = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']
        check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
        # =======================================================================
        # 根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置，例如：2,4
        # ---------------------------------------
        #         |         |         |
        #    0    |    1    |    2    |     3
        #         |         |         |
        # ---------------------------------------
        #         |         |         |
        #    4    |    5    |    6    |     7
        #         |         |         |
        # ---------------------------------------
        # 生成索引与坐标对应的字典
        ret = {str(idx):location for idx,location in enumerate(view_location)}
        # print(ret)
        # ret:
        # {'0': '35,35', '1': '105,35', '2': '175,35', '3': '245,35', '4': '35,105', '5': '105,105', '6': '175,105', '7': '245,105'}
        user_idx = input('请输入图片索引号，以逗号分隔(例子：2,4): ')
        user_str = ''
        # 拼接坐标字符串
        for x in user_idx.split(','):
            user_str += '{},'.format(ret[x])
        # 去掉最后那个逗号
        user_str = user_str[0:-1]
        # 以逗号分隔合并
        verify_location = ','.join(user_str.split(','))
        # 构造提交验证码接口数据格式
        data = {
            # 固定的
            'login_site': 'E',
            # 固定的
            'rand': 'sjrand',
            # 验证码对应的坐标，两个为一组，选择了几个正确的，输入几个
            'answer': verify_location
        }
        # print(data)
        # 提交数据
        content = self.session.post(url=check_url, data=data, headers=self.agent_header, verify=False)
        # 获取返回结果，并将返回结果转成json格式
        result_dic = json.loads(content.content)
        # 获取状态码
        code = result_dic['result_code']
        # 取出验证结果，4：成功  5：验证失败  7：过期
        # print(code)
        if int(code) == 4:
            return True
        else:
            return False

    def main_login(self):
        '''
        登陆接口
        '''
        # 获取用户名及密码
        username = input('Please input your UserName:')
        # 这个需要在命令行执行，才能看出效果(隐藏密码)
        psswd = getpass.getpass('Please input your Password:')
        loginurl = "https://kyfw.12306.cn/passport/web/login"
        # 构造提交登陆数据格式
        data = {
            'username': username,
            'password': psswd,
            # 固定的
            'appid': 'otn'
        }
        # 提交请求并获取返回结果
        result = self.session.post(url=loginurl, data=data, headers=self.agent_header, verify=False)
        # 获取返回结果，并将返回结果转成json格式
        result_dic = json.loads(result.content)
        # 获取返回结果文字
        msg = result_dic['result_message']
        # 结果的编码方式是Unicode编码，所以对比的时候字符串前面加u,或者mes.encode('utf-8') == '登录成功'进行判断，否则报错
        if msg == '登录成功':
            print('恭喜你，登录成功，可以购票!')
        else:
            print('对不起，登录失败，请检查登录信息!')

if __name__ == '__main__':
    print('程序开始啦！！！！')
    # 生成实例
    login = Login()
    # 获取验证码图片
    login.get_authentication_photo()
    # 调用验证码验证结果并返回状态
    flag = login.Check_Authentication_Code()
    # print(flag)
    if flag:
        # 如果状态为True,继续调用登陆接口
        login.main_login()
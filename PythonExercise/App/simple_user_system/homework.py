import json
import getpass

class run():

    def __init__(self):
        '''
        初始化用户数据保存文件名
        初始化密码保存文件名
        初始化命令对应功能函数字典
        '''
        self.filename = 'store_file.json'
        self.passwd = 'passwd_file.json'
        self.action_dict = {
            'delete': self.new_delete,
            'update': self.new_update,
            'find': self.new_find,
            'show': self.new_show,
            'exit': self.new_exit
        }

    def new_delete(self):
        '''
        删除用户功能
        '''
        user = input('请输入需要删除的用户名：').strip('\r')
        for k,v in self.new_dict.items():
            # 删除索引对应的数据
            if user == v["username"]:
                del self.new_dict[k]
                break
        else:
            print('您想删除的用户不存在')

    def new_update(self):
        '''
        添加用户功能
        '''
        num_max = 0
        for k, v in self.new_dict.items():
            # 获取目前索引的最大值
            if int(k) > num_max:
                num_max = int(k)

        # 索引最大值+1(类似于数据库的自增序列)
        num_max += 1
        print('输入格式： 用户名:年龄:联系方式')
        user,age,tel = input('>>> ').split(':')
        # 数据写入字典
        self.new_dict[str(num_max)] = {
          "username": user,
          "age":age,
          "tel":tel
              }


    def new_find(self):
        '''
        查找用户名
        '''
        user = input('请输入需要查找的用户名：')
        for k,v in self.new_dict.items():
            # 在字典中查找匹配数据
            if user == v["username"]:
                print('用户名:{} 年龄:{} 电话:{}'.format(v["username"],v["age"],v['tel']))
                break
        else:
            print('用户没找到')

    def new_show(self):
        '''
        展示所有用户名，并排序
        '''
        if self.new_dict:
            print('{:>20} |{:>20} |{:>20}'.format('username', 'age', 'tel'))
            field = input('请输入想要排序的字段(默认username):')
            # 默认对用户名排序
            if len(field) == 0 or field == 'username':
                # sorted函数可以方便地针对不同的数据结构进行排序
                # sorted用法详见https://www.jianshu.com/p/7be04a3f30cd
                for k,v in sorted(self.new_dict.items(),key=lambda e:e[1]['username']):
                    print('{:>20} |{:>20} |{:>20}'.format(v["username"],v["age"],v['tel']))
            else:
                if field == 'age':
                    for k, v in sorted(self.new_dict.items(), key=lambda e: int(e[1]['age'])):
                        print('{:>20} |{:>20} |{:>20}'.format(v["username"], v["age"], v['tel']))
                if field == 'tel':
                    for k, v in sorted(self.new_dict.items(), key=lambda e: int(e[1]['tel'])):
                        print('{:>20} |{:>20} |{:>20}'.format(v["username"], v["age"], v['tel']))

        else:
            print('目前啥都没有')

    def new_exit(self):
        '''
        退出，并持久化至文件
        '''
        answer = input('请问您想保存现有信息并退出吗？？[y/n]')
        if answer == 'y' or answer == 'Y':
            # 写入文件
            with open(self.filename, 'w') as fb2:
                fb2.write(json.dumps(self.new_dict, indent=4, sort_keys=True, ensure_ascii=False))
            exit(0)

    def main(self):
        print('程序启动啦！！！')
        # 读取密码文件并返回结果
        with open(self.passwd, 'r') as fb:
            self.passwd_dict = json.loads(fb.read())
        result = self.passwd_dict.get('password',None)
        # 如果密码文件为空，就写入新密码
        if result is None or result == '':
            passwd = getpass.getpass('由于是第一次登陆，请输入管理员密码:')
            with open(self.passwd, 'r') as fb2:
                self.passwd_dict = json.loads(fb2.read())
                self.passwd_dict['password'] = passwd
            with open(self.passwd, 'w') as fb3:
                fb3.write(json.dumps(self.passwd_dict, indent=4, sort_keys=True, ensure_ascii=False))
            print('管理员密码设置成功！！！')
        # 读取用户数据文件
        with open(self.filename, 'r') as fb1:
            self.new_dict = json.loads(fb1.read())
        while True:
            action = input(">>> ")
            if not action:
                continue
            if action in self.action_dict:
                passwd = getpass.getpass('请输入管理员密码:')
                # 检查密码是否一致
                if self.passwd_dict['password'] == passwd:
                    # 命令对应功能函数字典中找出对应方法并执行
                    func = self.action_dict.get(action)
                    func()
                else:
                    print('密码输入错误！！！')
            else:
                print('命令格式: [delete|update|find|show|exit]')


if __name__ == "__main__":
    f = run()
    f.main()

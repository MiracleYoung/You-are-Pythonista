from pymongo import MongoClient
from pymongo import ASCENDING
from pymongo import DESCENDING
import getpass

class run():

    def __init__(self):
        '''
        初始化数据库
        初始化用户表
        初始化密码表
        初始化命令对应功能函数字典
        '''
        self.client = MongoClient('127.0.0.1', 27017)
        self.db_name = 'wangtiejiang'
        self.db = self.client[self.db_name]
        self.collection_user = self.db['account']
        self.collection_passwd = self.db['passwd']
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
        for item in self.collection_user.find():
            # 删除索引对应的数据
            if user == item["用户名"]:
                self.collection_user.remove({'用户名': user })
                print('用户\'{}\'删除成功!'.format(user))
                break
        else:
            print('您想删除的用户不存在')

    def new_update(self):
        '''
        添加用户功能
        '''
        print('输入格式： 用户名:年龄:联系方式')
        user,age,tel = input('>>> ').split(':')
        # 数据写入字典
        self.collection_user.insert(
            {
             '用户名': user,
             '年龄': int(age),
             '电话': int(tel)
            }
        )
        print('用户信息录入成功!')


    def new_find(self):
        '''
        查找用户名
        '''
        user = input('请输入需要查找的用户名：')
        user_result = self.collection_user.find_one({'用户名': user })
        if user_result:
            print('用户名:{},年龄:{},联系方式:{}'.format(user_result['用户名'], user_result['年龄'], user_result['电话']))
        else:
            print('用户没找到')

    def new_show(self):
        '''
        展示所有用户名，并排序
        '''
        user_dict = {
            'user': '用户名',
            'age': '年龄',
            'tel': '电话'
        }
        sort_filed = input('请指定排序字段(默认不排序):')
        if sort_filed in ['user','age','tel']:
            for item in self.collection_user.find().sort(user_dict[sort_filed],ASCENDING):
                print('用户名:{},年龄:{},联系方式:{}'.format(item['用户名'],item['年龄'],item['电话']))
        else:
            for item in self.collection_user.find():
                print('用户名:{},年龄:{},联系方式:{}'.format(item['用户名'], item['年龄'], item['电话']))

    def new_exit(self):
        '''
        退出程序
        '''
        answer = input('请问您想退出吗??[y/n]')
        if answer == 'y' or answer == 'Y':
            exit(1)

    def new_changepasswd(self):
        '''
        修改密码
        '''
        user_input_old_passwd = getpass.getpass('准备修改管理员密码，请输入原密码:')
        for item in self.collection_passwd.find():
            if item['密码']:
                self.passwd = item['密码']
            break
        if self.passwd == '':
            print('密码异常,请检查数据库')
        if user_input_old_passwd == self.passwd:
            while True:
                count = 0
                user_input_new_passwd = getpass.getpass('准备修改管理员密码，请输入新密码:')
                if user_input_old_passwd == user_input_new_passwd:
                    if  count > 3:
                        print('输入次数过多')
                        break
                    print('新密码和旧密码一样，请重新输入')
                    count += 1
                else:
                    self.collection_passwd.remove()
                    self.collection_passwd.insert({'密码': user_input_new_passwd})
                    print('密码修改成功')
                    break





    def main(self):
        print('程序启动啦！！！')
        while True:
            for item in self.collection_passwd.find():
                if item['密码']:
                    self.passwd_in_mongo = item['密码']
                break
            # print(self.passwd_in_mongo)
            action = input(">>> ").strip('\r')
            if not action:
                continue
            if action == 'change':
                self.new_changepasswd()
            elif action in self.action_dict:
                user_input_passwd = getpass.getpass('请输入管理员密码:')
                # 检查密码是否一致
                if  self.passwd_in_mongo == user_input_passwd:
                    # 命令对应功能函数字典中找出对应方法并执行
                    func = self.action_dict.get(action)
                    func()
                else:
                    print('密码输入错误！！！')
            else:
                print('命令格式: [delete|update|find|show|exit|change]')


if __name__ == "__main__":
    f = run()
    f.main()
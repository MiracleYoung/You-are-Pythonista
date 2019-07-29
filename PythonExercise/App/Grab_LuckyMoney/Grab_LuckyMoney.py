from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def Grab_LuckyMoney():

    # 获取消息列表元素
    CurrentPage_msg_list = poco("android.widget.ListView").children()
    # 把获取到的消息，反序存储，以便从最新的红包开始抢起
    msg_list = []
    for i in CurrentPage_msg_list:
        msg_list.insert(0, i)

    # 遍历消息并查找红包
    for msg in msg_list:

        # 微信红包的标识
        LuckyMoney = msg.offspring('com.tencent.mm:id/aql')
        # 已失效红包（比如已领取、已被领完）的标识
        Invalid = msg.offspring('com.tencent.mm:id/aqk')

        # 判断红包是否有效并抢起来！
        if LuckyMoney:
            print(f'红包！红包！')
            if Invalid.exists() and (Invalid.get_text()=='已领取' or Invalid.get_text()=='已被领完'):
                print(f'红包已无效，跳过……')
                continue
            else:
                print(f'发现一个新红包，抢起来！')
                poco("com.tencent.mm:id/d1v")
                msg.click()

                click_open = poco("com.tencent.mm:id/d02")
                if click_open.exists():
                    click_open.click()
                keyevent('BACK')
        else:
            print(f'未发现红包……')
            continue



if __name__ == '__main__':

    # 打开手机微信
    poco(text='微信').click()

    # 群聊消息的元素标识
    Chat_msg = poco(name='com.tencent.mm:id/d1v').offspring('com.tencent.mm:id/b6e')
    # 获取当前页面中所有所有群聊的名称
    Chat_names = []
    Chat_names = list(map(lambda x: x.get_text(), Chat_msg))

    # 指定抢红包的群聊名称
    chat = input('请指定群聊名称:')
    if chat in Chat_names:
        index = Chat_names.index(chat)
        # 点击进入指定的群聊
        Chat_msg[index].click()

        while True:
            Grab_LuckyMoney()
            print(f'休眠1秒钟，继续刷新页面，开始抢红包')
            sleep(1)
    else:
        print(f'找不到这个群')

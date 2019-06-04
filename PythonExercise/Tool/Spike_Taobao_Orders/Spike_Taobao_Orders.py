from selenium import webdriver
import datetime
import time

def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"请尽快扫码登录")
        time.sleep(10)


def picking(method):
    # 打开购物车列表页面
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    # 是否全选购物车
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print(f"找不到购买按钮")
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(5)


def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print(f"抢购成功，请尽快付款")
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":

    # 请指定勾选购物车商品的方式
    # 0代表，自动勾选购物车内的全部商品。注意：若购物车中存在失效商品时无法进行全选，请勿使用此项
    # 1代表，手动勾选购物车内的商品
    method = 1

    # 请指定抢购时间，时间格式："2019-06-01 10:08:00.000"
    times = "2019-06-04 08:35:00.000"

    # 自动打开Chrome浏览器
    browser = webdriver.Chrome()
    # 设置浏览器最大化显示
    browser.maximize_window()

    # 扫码登录淘宝
    login()
    # 勾选准备结算的商品
    picking(method)
    # 等待抢购时间，定时秒杀
    buy(times)

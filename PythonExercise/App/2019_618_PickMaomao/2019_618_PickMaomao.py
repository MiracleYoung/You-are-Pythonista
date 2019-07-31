import os,time

def pick_maomao():
    print(f"点 合合卡 按钮")
    os.system('adb shell input tap 145 1625')
    time.sleep(1)
    print(f"点 进店找卡 按钮")
    os.system('adb shell input tap 841 1660')
    time.sleep(13)
    print(f"猫猫出现啦，点击得喵币")
    os.system('adb shell input tap 967 1134')
    time.sleep(1)
    print(f"点 开心收下")
    os.system('adb shell input tap 569 1380')
    time.sleep(1)
    print(f"利用全面屏手势退出店铺")
    os.system('adb shell input swipe 0 1500 500 1500')
    time.sleep(1)


for i in range(40):
    pick_maomao()

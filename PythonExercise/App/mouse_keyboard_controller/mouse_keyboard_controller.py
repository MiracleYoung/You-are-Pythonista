#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/7/12 上午6:53
# @Author  : MiracleYoung
# @File    : mouse_keyboard_controller.py

# from pynput import mouse, keyboard

# from pynput.mouse import Controller, Button
#
# mouse = Controller()
#
# # 获取当前鼠标位置
# print(f'当前小胖的鼠标位置是： {mouse.position}')
#
# # 设置鼠标位置
# mouse.position = (10, 20)
# print(f'现在小胖把鼠标移动到 {mouse.position}')
#
# # 使用相对距离，移动当前鼠标
# mouse.move(5, -5)
#
# # 按下鼠标左键，释放鼠标左键
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # 向下滚动2格
# mouse.scroll(0, 2)

# from pynput import mouse
#
# def on_move(x, y):
#     print(f'鼠标移动到坐标 {(x, y)}')
#
# def on_click(x, y, button, pressed):
#     print(f"{'按下' if pressed else '释放'} ，当前位置是： {(x, y)}")
#     if not pressed:
#         # 停止监听
#         return False
#
# def on_scroll(x, y, dx, dy):
#     print(f"滑动鼠标， {'向下' if dy < 0 else '向上'} at {(x, y)}")
#
# # 一直监听事件，直到鼠标释放
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()


# from pynput.keyboard import Key, Controller
#
# keyboard = Controller()
#
# # 按下并释放空格
# keyboard.press(Key.space)
# keyboard.release(Key.space)
#
# # 按下并释放小写字母a
# keyboard.press('a')
# keyboard.release('a')
#
# # 2种方式输入大写A
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')
#
# # 直接操作键盘输入Hello World
# keyboard.type('Hello World')


from pynput import keyboard

def on_press(key):
    try:
        print(f'字母 {key.char} 被按下了')
    except AttributeError:
        print(f'特殊的键 {key} 被按下了')

def on_release(key):
    print(f'{key} 被释放了')
    if key == keyboard.Key.esc:
        # 停止监听
        return False

# 一直监听键盘事件，直到停止
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
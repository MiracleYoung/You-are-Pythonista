import pygame
import random

def draw_button(screen, text, position, right=False):
    '''
    绘制文本按钮
    :param screen: 绘制在哪一个屏幕上
    :param text: 绘制的文本
    :param position: 绘制的位置
    :param right: 是否为右边
    :return: 返回一个4个元素的元祖，即button的开始位置，结束位置
    '''
    # 得到系统文件中的 '华文中宋' 字体， 设置字体大小为30px
    font = pygame.font.SysFont('华文中宋', 30)
    # 得到一个pygame.Surface对象， 绘制的时候需要这个对象
    # text：绘制的文本
    # antialias： True or False 是否为锯齿状
    # color： 字体颜色
    # background：背景颜色
    button = font.render(text, True, (0,0,0),(96,96,96))
    # 得到button的大小，width和height,返回的是一个两个元素的元祖
    button_size = button.get_size()
    # 如果right=Ture， 表示是绘制在右边的button，就让它的位置和背景图右对齐
    if right:
        position = position[0]-button_size[0], position[1]
    # 在position位置处绘制button， position是一个两个元素的元祖， button是一个pygame.Surface对象
    screen.blit(button, position)
    # 返回一个4个元素的元祖，即button的开始位置，结束位置
    return (position[0], position[1], position[0]+button_size[0], position[1]+button_size[1])

def position_is_in_rect(position, rect):
    '''
    检查position是否在一个矩形内区域内,
    :param position: 需要判断的position
    :param rect: 在哪一个矩形区域内？
    :return: True or False
    '''
    if position[0] >= rect[0] and position[0] <= rect[2]:
        if position[1] >= rect[1] and position[1] <= rect[3]:
            return True
    return False

def get_random_position(size=(300, 480)):
    '''
    得到随机位置
    :param size: 窗口的大小
    :return: 返回一个两个元素的元祖
    '''
    x = random.randint(0, size[0])
    y = random.randint(0, size[1]-50)
    return x, y

def main():
    # 初始化pygame
    pygame.init()

    # 规定窗口的大小
    size = 300, 480
    # 得到一这个窗口
    screen = pygame.display.set_mode(size)
    # 设置窗口的标题
    pygame.display.set_caption('表白神器')

    # 加载图片
    image = pygame.image.load('./images/biaobai.png').convert_alpha()
    # 得到图片的尺寸
    image_size = image.get_size()

    # 计算图片的放置位置， 在窗口中间
    position_x = (size[0]-image_size[0]) / 2
    position_y = (size[1]-image_size[1]) / 2

    # 存放所有的button的位置
    buttons_position = {}
    # 是否点击 yes按钮了
    yes = False
    # 是否改变否定按钮的位置
    change_position = False
    # 随机位置
    random_position = None

    while True:
        # 遍历所有的事件
        for event in pygame.event.get():
            # 如果点击关闭窗口， 程序结束
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            # 鼠标点击事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 得到鼠标点击位置
                click_position = pygame.mouse.get_pos()
                # 调用这个函数判断点击位置是否在yes按钮范围内
                if position_is_in_rect(click_position, buttons_position['yes']):
                    # 加载另外一张图片
                    image = pygame.image.load('./images/yes.jpg').convert_alpha()
                    # 修改yes变量为True
                    yes = True
                # 判断点击位置时候在no按钮区域内
                elif position_is_in_rect(click_position, buttons_position['no']):
                    # 死循环
                    while True:
                        # 得到随机位置
                        random_position = get_random_position()
                        # 如果随机位置不在yes按钮内，退出死循环
                        if not position_is_in_rect(random_position, buttons_position['yes']):
                            break
                    # 修改change_position变量为True
                    change_position = True

        # 填充整个窗口为白色
        screen.fill((255,255,255))
        # 将图片绘制到窗口中
        screen.blit(image, (position_x, position_y))

        # 如果没有点击yes按钮
        if not yes:
            # 绘制yes按钮
            yes_rect_region = draw_button(screen, '好的', (position_x, position_y + image_size[1] + 10))
            # 如果change_position为True，说明需要开始随机获取no按钮的位置
            # 绘制no按钮
            if change_position:
                no_rect_region = draw_button(screen, '考虑一下', random_position)
            else:
                no_rect_region = draw_button(screen, '考虑一下', (position_x + image_size[0], position_y + image_size[1] + 10), right=True)
            # 将yes按钮和no按钮的所在区域（一个4各元素的元祖，也就是矩阵）存放到buttons_position字典中
            buttons_position['yes'] = yes_rect_region
            buttons_position['no'] = no_rect_region

        # 刷新页面内容
        pygame.display.update()

if __name__ == '__main__':
    main()
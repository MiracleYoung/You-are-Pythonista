import numpy as np
from PIL import Image


def to_pixelBlock(pixel, Start_coordinate, End_coordinate):
    '''
    :param pixel: 单位像素块的元素大小
    :param Start_coordinate: 处理的起始坐标(像素)点，元组形式
    :param End_coordinate: 处理的终止坐标(像素)点，元组形式
    :return:
    通过中间值的RGB，对所选范围块的RGB进行重新赋值，设置的单位像素块(Pixel数值)越小， 生成的像素图越精确
    '''
    # 读取图片，并由 PIL image 转换为 NumPy array
    im1 = np.array(Image.open("P:\\Personal\\LuoShen.jpg"))
    
    # 遍历所要处理范围内的所有坐标(像素)点
    for y in range(Start_coordinate[1], End_coordinate[1], pixel):
        for x in range(Start_coordinate[0], End_coordinate[0], pixel):
            # 通过中间值的RGB，对所选范围块的RGB进行重新赋值，设置的单位像素块(Pixel数值)越小， 生成的像素图越精确
            im1[y:y + pixel, x:x + pixel] = im1[y + (pixel // 2)][x + (pixel // 2)]

    # 将NumPy array 转换为 PIL image  
    im2 = Image.fromarray(im1.astype(np.uint8))
    # 展示处理后的图像
    im2.show()


if __name__ == '__main__':
    # 设置好要处理的像素范围，并以多大的像素块来生成最终效果图
    to_pixelBlock(10, (0, 0), (1280, 800))

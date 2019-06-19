import numpy as np
from PIL import Image


def to_pixelBlock(pixel, start, end):
    # 读取图片，并由 PIL image 转换为 NumPy array
    im1 = np.array(Image.open("P:\\Personal\\LuoShen.jpg"))

    for y in range(start[1], end[1], pixel):
        for x in range(start[0], end[0], pixel):
            # 主要通过中间值的RGB，对所选范围块的RGB做修改，pixel值越小越精确
            im1[y:y + pixel, x:x + pixel] = im1[y + (pixel // 2)][x + (pixel // 2)]

    # 将NumPy array 转换为 PIL image  
    im2 = Image.fromarray(im1.astype(np.uint8))
    # 展示处理后的图像
    im2.show()


if __name__ == '__main__':
    '''通过选中范围的中间值颜色数组处理为像素块'''
    to_pixelBlock(10, (0, 0), (1280, 800))

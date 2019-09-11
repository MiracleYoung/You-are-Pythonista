import qrcode
import zxing
from MyQR import myqr
from PIL import Image
import os

def first_demo():
    qr = qrcode.make('Hello World')
    qr.get_image().show()

def second_demo():
    text = 'Python专栏'
    img = qrcode.make(text)
    img.save('qr.png')
    img.show()

def create_icon_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # 二维码图片的大小
        box_size=10,
        # 边框的大小
        border=2
    )

    # 添加数据
    qr.add_data('小可爱你好，我是波多野结衣老湿')
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color='grey',back_color='white')
    # 图片的宽，高
    img_w, img_h = img.size


    # 添加logo
    icon = Image.open('girl.jpg')

    # 设置log的大小
    factor = 3
    size_w = img_w // factor
    size_h = img_h // factor

    icon_w,icon_h = icon.size

    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h

    # 重新设置logo的尺寸
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)
    # 得到在二维码中显示的位置，坐标。
    w =  (img_w - icon_w) // 2
    h =  (img_h - icon_h) // 2

    img.paste(icon,(w,h),mask=None)
    img.save('girl.png')

def parse_qrcode(filename):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(filename)
    print(barcode.parsed)

def myqr_demo():
    words = 's'
    version, level, qr_name = myqr.run(
        words=words,
        version=10,
        picture='girl.jpg',
        colorized=True,
        save_name='girl_img.png',
        save_dir=os.getcwd()
    )
    print(version,level,qr_name)

if __name__ == '__main__':
    # first_demo()
    # second_demo()
    # myqr_demo()
    # parse_qrcode('qr.png')
    create_icon_qrcode()
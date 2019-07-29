# @Time    : 2019/07/12 20:55PM
# @Author  : HGzhao
# @File    : Wechat_Photo_Wall.py

from wxpy import *
import PIL.Image as Image
import os
import sys

# 获取文件所在的绝对路径
def get_dir(sys_arg):
	sys_arg = sys_arg.split("/")
	dir_str = ""
	count = 0
	for cur_dir in sys_arg:
		if count == 0:
			count = count + 1
		if count == len(sys_arg):
			break
		dir_str = dir_str + cur_dir + "/"
		count = count + 1
	return dir_str


# 完成好友头像的获取及下载
def get_imgs():

	# 获取当前路径信息
	curr_dir = get_dir(sys.argv[0])
	# 如果FriendImgs目录不存在就创建一个
	if not os.path.exists(curr_dir + "FriendImgs/"):
		os.mkdir(curr_dir + "FriendImgs/")

	# 登录微信并获取好友信息
	bot = Bot()
	my_friends = bot.friends(update=True)
	# 获取好友头像信息并存储在FriendImgs目录中
	n = 0
	for friend in my_friends:
		friend.get_avatar(curr_dir + "FriendImgs/" + str(n) + ".jpg")
		n = n + 1

# 用于制作生成照片墙
def to_Photo_Wall():

	# 准备生成微信好友头像墙的尺寸
	image = Image.new("RGB", (650, 650))

	# 定义初始图片的位置
	x = 0
	y = 0

	# 获取下载的头像文件
	curr_dir = get_dir(sys.argv[0])
	ls = os.listdir(curr_dir + 'FriendImgs')

	# 遍历文件夹的图片
	for file_names in ls:
		try:
			# 依次打开图片
			img = Image.open(curr_dir + "FriendImgs/" + file_names)
		except IOError:
			continue
		else:
			# 重新设置图片的大小
			img = img.resize((50, 50), Image.ANTIALIAS)
			# 将图片粘贴到最终的照片墙上
			image.paste(img, (x * 50, y * 50))
			# 设置每一行排13个图像
			x += 1
			if x == 13:
				x = 0
				y += 1
	# 保存图片为WeChat_Friends.jpg		
	img = image.save(curr_dir + "WeChat_Friends.jpg")


if __name__=='__main__':
	get_imgs()
	to_Photo_Wall()

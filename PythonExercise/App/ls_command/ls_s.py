# 颜色语法： \033[显示方式;前景色;背景色m 这种方法在windows cmd中不适用
import os
import argparse
import datetime
import ctypes
import sys
import win32com.client

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
# 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARK_BLUE = 0x01  # dark blue.
FOREGROUND_DARK_GREEN = 0x02  # dark green.
FOREGROUND_DARK_SKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARK_RED = 0x04  # dark red.
FOREGROUND_DARK_PINK = 0x05  # dark pink.
FOREGROUND_DARK_YELLOW = 0x06  # dark yellow.
FOREGROUND_DARK_WHITE = 0x07  # dark white.
FOREGROUND_DARK_GRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.

# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_DARK_BLUE = 0x10  # dark blue.
BACKGROUND_DARK_GREEN = 0x20  # dark green.
BACKGROUND_DARK_SKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARK_RED = 0x40  # dark red.
BACKGROUND_DARK_PINK = 0x50  # dark pink.
BACKGROUND_DARK_YELLOW = 0x60  # dark yellow.
BACKGROUND_DARK_WHITE = 0x70  # dark white.
BACKGROUND_DARK_GRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

###############################################################

# 暗蓝色
# dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARK_BLUE)
    sys.stdout.write(mess)
    resetColor()

# 暗绿色
# dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARK_GREEN)
    sys.stdout.write(mess)
    resetColor()

# 暗天蓝色
# dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARK_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()

# 暗红色
# dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARK_RED)
    sys.stdout.write(mess)
    resetColor()

# 暗粉红色
# dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARK_PINK)
    sys.stdout.write(mess)
    resetColor()

# 暗黄色
# dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARK_YELLOW)
    sys.stdout.write(mess)
    resetColor()

# 暗白色
# dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARK_WHITE)
    sys.stdout.write(mess)
    resetColor()

# 暗灰色
# dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARK_GRAY)
    sys.stdout.write(mess)
    resetColor()

# 蓝色
# blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()

# 绿色
# green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()

# 天蓝色
# sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()

# 红色
# red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()

# 粉红色
# pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()

# 黄色
# yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()

# 白色
# white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()

##################################################

# 白底黑字
# white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()

# 白底黑字
# white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()

# 获取快捷方式文件的原地址
# shell = win32com.client.Dispatch("WScript.Shell")
# shortcut = shell.CreateShortCut("ls.py-lnk.lnk")
# print(shortcut.Targetpath)

FILE_TYPE = {
    'dir': '\\',
    'exe': '*',
    'lnk': '@',
}

DETAIL_HEADER = '{:<15}\t{:<15}\t{:<8}\t{}'.format('创建时间', '修改时间', '文件大小', '文件名')
FILE_DETAIL_FORMAT = '{create_time:<20}\t{modify_time:<20}\t{file_size:<10}\t{file_name}'

class ShowFile:
    # 文件夹, 蓝色
    @classmethod
    def show_directory(cls,message):
        printBlue(message)

    # exe文件, 红色
    @classmethod
    def show_exe_file(cls, message):
        printRed(message)

    # py文件 黄色
    @classmethod
    def show_py_file(cls, message):
        printYellow(message)

    # 隐藏文件 绿色
    @classmethod
    def show_hide_file(cls, message):
        printGreen(message)

    # lnk文件 天蓝色
    @classmethod
    def show_lnk_file(cls, message):
        printSkyBlue(message)

    @classmethod
    def show_normal_file(cls, message):
        printWhite(message)

class LsCommand:
    def __init__(self, show_all=False, directory='.', end='\t', add_file_type=False, show_detail=False, recursion=False, shortcut=False):
        self.show_all = show_all
        self.directory = directory
        self.end = end
        self.add_file_type = add_file_type
        self.show_detail = show_detail
        self.recursion = recursion
        self.shortcut = shortcut
        if self.show_detail:
            print(DETAIL_HEADER)
            self.end = '\n'
        if self.shortcut:
            self.add_file_type = False

    def get_message(self, file, prefix=''):
        file_name = os.path.basename(file)
        if not self.show_detail:
            return file_name

        stat_result = os.stat(file)

        file_size = stat_result.st_size/1000

        message = FILE_DETAIL_FORMAT.format(**{
            'create_time' : datetime.datetime.fromtimestamp(stat_result.st_ctime).strftime('%Y-%m-%d %H:%M'),
            'modify_time' : datetime.datetime.fromtimestamp(stat_result.st_mtime).strftime('%Y-%m-%d %H:%M'),
            'file_size' : str(file_size)+'k',
            'file_name' : prefix + file_name
        })

        return message

    def get_lnk_file_source_path(self, path):
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        return shortcut.Targetpath

    def show_file_info(self, abs_path, prefix=''):

        file_type_str = ''
        file = os.path.basename(abs_path)
        message = self.get_message(abs_path, prefix)

        if os.path.isdir(abs_path):
            if self.add_file_type:
                file_type_str = FILE_TYPE.get('dir')
            ShowFile.show_directory(message + file_type_str + self.end)
        elif file.endswith('.exe'):
            if self.add_file_type:
                file_type_str = FILE_TYPE.get('exe')
            ShowFile.show_exe_file(message + file_type_str + self.end)
        elif file.startswith('.'):
            ShowFile.show_hide_file(message + self.end)
        elif file.endswith('.py'):
            ShowFile.show_py_file(message + self.end)
        elif file.endswith('.lnk'):
            if self.add_file_type:
                file_type_str = FILE_TYPE.get('lnk')

            if self.shortcut:
                source_abs_path = self.get_lnk_file_source_path(abs_path)
                ShowFile.show_lnk_file(message + file_type_str + ' -> ' + source_abs_path + '\n')
            else:
                ShowFile.show_lnk_file(message + file_type_str + self.end)
        else:
            ShowFile.show_normal_file(message + self.end)

    def handle_directory(self, path, grade=1, prefix='--'):
        if not os.path.exists(path):
            raise ValueError(f'{path} not exists')

        if not os.path.isdir(path):
            raise ValueError(f'{path} not a directory')

        add_grade = False
        for file in os.listdir(path):

            if not self.show_all:
                if file.startswith('.'):
                    continue

            abs_path = os.path.join(path, file)
            self.show_file_info(abs_path, prefix=grade * prefix + " ")
            if os.path.isdir(abs_path):
                if not add_grade:
                    grade += 1
                self.handle_directory(abs_path, grade=grade)

    def run(self):
        for file in os.listdir(self.directory):
            abs_path = os.path.join(self.directory, file)

            if not self.show_all:
               if file.startswith('.'):
                   continue

            self.show_file_info(abs_path)

            if self.recursion:
                if os.path.isdir(abs_path):
                    self.handle_directory(abs_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ls', usage='显示文件夹下面的文件')

    parser.add_argument('-a', '--all', const=True, nargs='?', help='是否显示隐藏文件')
    parser.add_argument('-d', '--directory', help='指定文件夹')
    parser.add_argument('-l', const=True, nargs='?', help='单列显示，每个文件后面都换行')
    parser.add_argument('-C', const=True, nargs='?', help='多列显示，每个文件后面不换行, 这是默认值, 没有颜色')
    parser.add_argument('-F', const=True, nargs='?', help=r'在每个文件夹后追加类型表示符, *:exe文件, \:文件夹, @:快捷方式文件')
    parser.add_argument('-S', const=True, nargs='?', help='显示文件的详细信息')
    parser.add_argument('-R', const=True, nargs='?', help='递归显示子目录下面的文件信息')
    parser.add_argument('-shortcut', const=True, nargs='?', help='如果文件为快捷方式，显示出源文件地址')

    arg = parser.parse_args()

    show_all = arg.all or False
    directory = arg.directory or '.'
    end = '\t'
    if arg.C:
        end = '\t'
    if arg.l:
        end = '\n'

    F = arg.F or False
    show_detail = arg.S or False

    recursion = arg.R or False
    shortcut = arg.shortcut or False

    ls = LsCommand(show_all=show_all, directory=directory, end=end, add_file_type=F, show_detail=show_detail, recursion=recursion, shortcut=shortcut)
    ls.run()

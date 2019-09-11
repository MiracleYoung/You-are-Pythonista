import os
import argparse

class LsCommand():
    def __init__(self, show_all=False, directory='.', recursion=False):
        '''
        :param show_all: 是否显示隐藏文件
        :param directory: 指定的文件目录
        :param recursion: 是否递归显示目录下的文件
        '''
        self.show_all = show_all
        self.recursion = recursion
        self.directory = os.path.abspath(directory)

    def handle_dir(self, directory, grade=1, placeholder='--'):
        '''
        处理目录
        :param directory: 文件目录
        :param grade: 目录层级
        :param placeholder: 子目录文件前面的占位符
        :return:
        '''

        # 判断是否为文件夹
        if not os.path.isdir(directory):
            raise ValueError(f'{directory} is not a directory ')

        # grade是否增加过了
        grade_is_add = False

        # os.listdir: 列出当前文件夹下面的所有文件和文件夹
        # 遍历目录下的文件，文件夹
        for file in os.listdir(directory):
            # 构造绝对路径
            abs_path = os.path.join(directory, file)
            # 子目录，子文件打印的前缀
            prefix = grade * placeholder + ' '
            # 显示文件名
            self.show_file_or_dir(abs_path, prefix)

            # 如果是目录
            if os.path.isdir(abs_path):
                # 如果层级还没有增加，就增加一
                if not grade_is_add:
                    grade += 1

                # 继续进入处理目录的函数
                self.handle_dir(abs_path, grade=grade)

    def show_file_or_dir(self, file, prefix=''):

        # 如果不显示隐藏文件
        if not self.show_all:
            # os.path.basename(file) 只得到文件名,
            # 如果文件名是以'.'开始的，就直接返回，不打印
            if os.path.basename(file).startswith('.'):
                return

        # 打印前缀和文件名
        print(prefix + os.path.basename(file))

    def run(self):
        '''
        运行ls命令
        :return:
        '''

        # os.listdir(dir) 得到dir目录下所有文件，文件夹
        # 遍历self.directory目录先所有文件，文件夹
        for file in os.listdir(self.directory):
            # 构造绝对路径
            abs_path = os.path.join(self.directory, file)
            # 显示文件信息
            self.show_file_or_dir(abs_path)

            # 如果递归显示
            if self.recursion:
                # 如果是文件夹
                if os.path.isdir(abs_path):
                    # 进入处理文件夹的函数
                    self.handle_dir(abs_path)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='ls', description='显示文件夹下的文件')
    parser.add_argument('-a', '--all', const=True, nargs='?', help='是否显示隐藏文件')
    parser.add_argument('-d', '--directory', help='指定显示的目录，如果不指定，默认为当前目录')
    parser.add_argument('-r', '--recursion', const=True, nargs='?', help='是否递归显示')

    args = parser.parse_args()
    directory = args.directory
    if directory:
        if not os.path.exists(directory):
            raise ValueError(f'{directory} does`t exist')

        if not os.path.isdir(directory):
            raise ValueError(f'{directory} is not a directory')

    else:
        directory = '.'

    ls = LsCommand(bool(args.all), directory, bool(args.recursion))
    ls.run()


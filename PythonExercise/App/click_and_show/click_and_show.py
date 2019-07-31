from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QLineEdit
import sys

class App(QWidget):

    def __init__(self):
        '''
        初始化操作
        '''
        # 调用父类QWidget的方法
        super().__init__()
        # 对话框标题文字
        self.title = '人人都是Pythonista'
        # 对话框初始显示位置(从屏幕左边开始往右数)
        self.left = 200
        # 对话框的初始高度(从屏幕上面开始往下数)
        self.top = 250
        # 对话框宽
        self.width = 500
        # 对话框高
        self.height = 500
        # 初始化时执行页面ui初始化方法
        self.initUI()


    def initUI(self):
        '''
        页面ui初始化
        '''
        # 设置窗口标题
        self.setWindowTitle(self.title)
        # 设置窗口初始位置
        self.setGeometry(self.left, self.top, self.width, self.height)
        # 设置窗口小图标(icon)
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        # 创建文本框
        self.textbox = QLineEdit(self)
        # 文本框在界面中的初始位置(左上角的位置)
        self.textbox.move(20, 30)
        # 文本框的尺寸(长，宽)
        self.textbox.resize(400, 300)

        # 创建一个按钮
        self.button = QPushButton('在这里点击', self)
        # 按钮的初始位置(左上角的位置)
        self.button.move(20, 340)

        # 将按钮点击事件与下面的on_click方法关联起来
        self.button.clicked.connect(self.on_click)
        # 弹出对话框
        self.show()

    @pyqtSlot()
    def on_click(self):
        '''
        点击事件
        '''
        # 获取文本框中输入的值
        textboxValue = self.textbox.text()
        # 弹出对话框
        QMessageBox.question(self, "这里是消息框", '你输入了这些内容:' + textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        # 点击以后清空文本框
        self.textbox.setText('')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    exec = App()
    sys.exit(app.exec_())
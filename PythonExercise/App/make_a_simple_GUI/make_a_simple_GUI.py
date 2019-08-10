import tkinter as tk
import tkinter.messagebox as mbox

# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master = None):
        # 初始化Application的Frame部分 
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        # 创建控件
        self.createWidgets()

    # 创建控件
    def createWidgets(self):
        # 创建一个标签，输出要显示的内容
        self.firstLabel = tk.Label(self,text="「人人都是Pythonista」专注Python领域，做最专业的Python星球。")
        # 设定使用grid布局
        self.firstLabel.grid()
        # 创建一个按钮，用来触发answer方法
        self.clickButton = tk.Button(self,text="点一下瞧瞧？",command=self.answer)
        # 设定使用grid布局
        self.clickButton.grid()

    def answer(self):
        # 我们通过 messagebox 来显示一个提示框
        mbox.showinfo("「人人都是Pythonista」",'''
        这是一个专注Python的星球，我们提供「从零单排」、「实战项目」、「大航海」、「技术沙龙」、「技术分享」、「大厂内推」等系列供你选择及学习，当然也会有周边技术沿伸。
        本星球会不定期开展各类实战项目，阶段性组织线上技术沙龙、分享等；对于职业发展路线不明确的，我们会邀请到一些大厂hr及高级开发、经理等给大家解惑。
        加入我们，和千人一起玩Python，To be a Pythonista！
        ''')

# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('「人人都是Pythonista」')
# 设置窗体大小
app.master.geometry('400x100')
# 主循环开始
app.mainloop()

class SudoKu():
    def __init__(self,sudo_ku_data):
        if not isinstance(sudo_ku_data,list):
            raise TypeError(f'sudo_ku_data params must a list, but {sudo_ku_data} is a {type(sudo_ku_data)}')

        if len(sudo_ku_data) != 9 or len(sudo_ku_data[0]) != 9:
            raise TypeError(f'sudo_ku_data params must a 9*9 list, but {sudo_ku_data} is a {len(sudo_ku_data)}*{len(sudo_ku_data[0])} list')

        self.sudo_ku = sudo_ku_data
        # 存放每一行已有的数据
        self.every_row_data = {}
        # 每一列已有的数字
        self.every_column_data = {}
        # 每一个3*3有的数字
        self.every_three_to_three_data = {}
        # 每一个空缺的位置
        self.vacant_position = []
        # 每一个空缺位置尝试了的数字
        self.every_vacant_position_tried_values = {}

        # 初始化数据
        self._init()

    def _add_row_data(self,row,value):
        '''
        初始化的时候
        添加数据到self.every_row_data中
        :param row:
        :param value:
        :return:
        '''
        if row not in self.every_row_data:
            self.every_row_data[row] = set()

        if value in self.every_row_data[row]:
            raise TypeError(f'params {self.sudo_ku} is a invalid SudoKu')

        self.every_row_data[row].add(value)

    def _add_column_data(self,column,value):
        '''
        初始化的时候
        添加数据到self.every_column_data中
        :param column:
        :param value:
        :return:
        '''
        if column not in self.every_column_data:
            self.every_column_data[column] = set()

        if value in self.every_column_data[column]:
            raise TypeError(f'params {self.sudo_ku} is a invalid SudoKu')

        self.every_column_data[column].add(value)

    def _get_three_to_three_key(self,row,column):
        '''
        得到每一个3*3的key
        :param row:
        :param column:
        :return:
        '''
        if row in [0,1,2]:
            if column in [0,1,2]:
                key = 1
            elif column in [3,4,5]:
                key = 2
            else:
                key = 3
        elif row in [3,4,5]:
            if column in [0,1,2]:
                key = 4
            elif column in [3,4,5]:
                key = 5
            else:
                key = 6
        else:
            if column in [0,1,2]:
                key = 7
            elif column in [3,4,5]:
                key = 8
            else:
                key = 9

        return key

    def _add_three_to_three_data(self,row,column,value):
        '''
        初始化的时候
        添加数据到self.every_three_to_three_data中
        :param row:
        :param column:
        :param value:
        :return:
        '''
        key = self._get_three_to_three_key(row,column)

        if key not in self.every_three_to_three_data:
            self.every_three_to_three_data[key] = set()

        self.every_three_to_three_data[key].add(value)

    def _init(self):
        '''
        根据传入的数独，初始化数据
        :return:
        '''
        for row,row_datas in enumerate(self.sudo_ku):
            for column,value in enumerate(row_datas):
                if value == '':
                    self.vacant_position.append( (row,column) )
                else:
                    self._add_row_data(row,value)
                    self._add_column_data(column,value)
                    self._add_three_to_three_data(row,column,value)

    def _judge_value_is_legal(self,row,column,value):
        '''
        判断方放置的数据是否合法
        :param row:
        :param column:
        :param value:
        :return:
        '''

        # value是否存在这一行数据中
        if value in self.every_row_data[row]:
            return False
        # value是否存在这一列数据中
        if value in self.every_column_data[column]:
            return False

        # value是否存在这个3*3的宫内
        key = self._get_three_to_three_key(row,column)
        if value in self.every_three_to_three_data[key]:
            return False

        return True

    def _calculate(self, vacant_position):
        '''
        计算，开始对数独进行放置值
        :param vacant_position:
        :return:
        '''
        # 得到当前位置
        row,column = vacant_position
        values = set(range(1,10))

        # 对当前为位置创建一个唯一key,用来存放当前位置已经尝试了的数据
        key = str(row) + str(column)
        # 如果这个key存在，就对values进行取差集，因为两个都是集合（set），直接使用-就行了
        if key in self.every_vacant_position_tried_values:
            values = values - self.every_vacant_position_tried_values[key]
        # 如果这个key不存在，就创建一个空的集合
        else:
            self.every_vacant_position_tried_values[key] = set()

        for value in values:
            # 对当前数据添加到当前位置尝试过的的数据中
            self.every_vacant_position_tried_values[key].add(value)
            # 如果当前value合法，可以放置
            if self._judge_value_is_legal(row,column,value):
                print(f'set {vacant_position} value is {value}')
                # 更新 判断数据合法时 需要使用到的数据
                self.every_column_data[column].add(value)
                self.every_row_data[row].add(value)
                key = self._get_three_to_three_key(row,column)
                self.every_three_to_three_data[key].add(value)

                # 修改这个位置的值为value
                self.sudo_ku[row][column] = value
                # 返回True 和填充的 value
                return True,value

        return False,None

    def _backtrack(self,current_vacant_position,previous_vacant_position,previous_value):
        '''
        回溯
        :param current_vacant_position: 当前尝试失败的位置
        :param previous_vacant_position: 上一次成功的位置
        :param previous_value:上一次成功的值
        :return:
        '''
        print(f"run backtracking... value is {previous_value},vacant position is {previous_vacant_position}")
        row,column = previous_vacant_position
        # 对上一次成功的值从需要用到的判断的数据中移除
        self.every_column_data[column].remove(previous_value)
        self.every_row_data[row].remove(previous_value)

        key = self._get_three_to_three_key(row,column)
        self.every_three_to_three_data[key].remove(previous_value)

        # 并且上一次改变的的值变回去
        self.sudo_ku[row][column] = ''

        # 对当前尝试失败的位置已经城市失败的的值进行删除，因为回溯了，所以下一次进来需要重新判断值
        current_row,current_column = current_vacant_position
        key = str(current_row) + str(current_column)
        self.every_vacant_position_tried_values.pop(key)

    def get_result(self):
        '''
        得到计算之后的数独
        :return:
        '''
        # 空缺位置的长度
        length = len(self.vacant_position)
        # 空缺位置的下标
        index = 0

        # 存放已经尝试了的数据
        tried_values = []
        # 如果index小于length,说明还没有计算完
        while index < length:
            # 得到一个空缺位置
            vacant_position = self.vacant_position[index]

            # 计入计算函数，返回是否成功，如果成功，value为成功 的值，如果失败，value为None
            is_success,value = self._calculate(vacant_position)
            # 如果成功，将value放在tried_values列表里面，因为列表是有序的.
            # index+1 对下一个位置进行尝试
            if is_success:
                tried_values.append(value)
                index += 1
            # 失败，进行回溯,并且index-1，返回上一次的空缺位置,我们需要传入当前失败的位置 和 上一次成功的位置和值
            else:
                self._backtrack(vacant_position,self.vacant_position[index-1],tried_values.pop())
                index -= 1

            # 如果index<0 了 说明这个数独是无效的
            if index < 0:
                raise ValueError(f'{self.sudo_ku} is a invalid sudo ku')

        # 打印计算之后的数独
        self.show_sudo_ku()
        return self.sudo_ku

    def show_sudo_ku(self):
        '''
        显示数独
        :return:
        '''
        for row in self.sudo_ku:
            print(row)

##################################################
#  用来判断最后计算的数独是否合法，和计算没有关系     #
##################################################

def judge_value_is_legal(row,column,value,sudo_ku):
    # column
    for i in range(0,9):
        if row == i:
            continue
        if value == sudo_ku[i][column]:
            return False

    # row
    for i in range(0,9):
        if column == i:
            continue
        if value == sudo_ku[row][i]:
            return False

    # three_to_three
    for i in range(row//3*3,row//3*3+3):
        for j in range(column//3*3,column//3*3+3):
            if i == row and j == column:
                continue
            if value == sudo_ku[i][j]:
                return False

    return True


def judge_sudo_ku_is_legal(sudo_ku):
    for row,row_values in enumerate(sudo_ku):
        for column,value in enumerate(row_values):
            if not judge_value_is_legal(row,column,value,sudo_ku):
                return False
    return True


if __name__ == '__main__':
    sudo_ku_data = [
        [5,3,'','',7,'','','',''],
        [6,'','',1,9,5,'','',''],
        ['',9,8,'','','','',6,''],
        [8,'','','',6,'','','',3],
        [4,'','',8,'',3,'','',1],
        [7,'','','',2,'','','',6],
        ['',6,'','','','',2,8,''],
        ['','','',4,1,9,'','',5],
        ['','','','',8,'','',7,9],
    ]
    sudo_ku_data2 = [
        [3, '', '', '', '', 1, '', '', ''],
        ['', '', 8, 6, '', '', '', 7, ''],
        ['', 4, '', '', '', '', '', 2, ''],
        [4, '', '', 2, '', '', 7, 5, 1],
        [9, '', 1, '', 8, '', 2, '', 6],
        ['', '', 7, 5, '', '', '', 3, 9],
        ['', 7, 9, '', '', 3, '', 1, 2],
        [6, 3, 2, '', 4, 5, 9, 8, 7],
        [8, 1, 4, '', '', 9, 5, 6, 3],
    ]
    sudo_ku_data3 = [
        [8, '', '', '', '', '', '', '', 4],
        ['', 2, '', '', '', '', '', 7, ''],
        ['', '', 9, 1, '', 6, 5, '', ''],
        ['', '', 6, 2, '', 8, 9, '', ''],
        ['', 9, '', '', 3, '', '', 4, ''],
        ['', '', 2, 4, '', 7, 8, '', ''],
        ['', '', 7, 9, '', 5, 6, '', ''],
        ['', 8, '', '', '', '', '', 2, ''],
        [6, '', '', '', '', '', '', '', 9],
    ]

    # 得到计算好的数独
    sudo_ku = SudoKu(sudo_ku_data3).get_result()

    # 判断最后生成的数独是否是有效的
    print(judge_sudo_ku_is_legal(sudo_ku))





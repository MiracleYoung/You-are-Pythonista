
class PlayingCard():
    format_playing_card_dict = {
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14,
        '2' : 15,
        'joker' : 16,
        'JOKER' : 17,
    }

    def __init__(self,left_card,right_card):
        self.left_card = self._format_playing_card(left_card)
        self.right_card = self._format_playing_card(right_card)
        self.function_map = {
            1: self._compare_first_value,  # 只用比较第一张牌的大小
            2: self._compare_has_two_joker,  # 有双王的比较
            3: self._compare_three_with_one,  # 都是三带一的比较
            4: self._compare_bomb_and_others,  # 一个炸弹和其他牌的比较
        }

    def _format_playing_card(self,cards):
        '''
        对手拍进行格式化，成为能直接比较的值
        :param cards: 手牌列表
        :return: 返回格式化好的列表
        '''
        for index,card in enumerate(cards):
            if card not in self.format_playing_card_dict:
                raise ValueError('请输入合法的牌')
            cards[index] = self.format_playing_card_dict[card]

        return cards

    def _show_playing_card(self,cards):
        '''
        对格式化之后的手牌改变回去
        :param cards: 格式化之后的手牌列表
        :return: 返回改变回去的手牌列表
        '''
        keys_list = list(self.format_playing_card_dict.keys())
        values_list = list(self.format_playing_card_dict.values())
        for index,card in enumerate(cards):
            key_index = values_list.index(card)
            cards[index] = keys_list[key_index]

        return cards

    def _get_every_value_repeat_count(self,cards):
        '''
        给传入的列表中的每个数计数
        => [7,7,7,4] : {7:3,4:1}
        => [7,7,7,7] : {7:4}
        :param cards: 牌的列表
        :return: 返回一个字典，包含不同的每张牌的个数
        '''
        temp_dict = {}
        for card in cards:
            if card not in temp_dict:
                temp_dict[card] = 1
            else:
                temp_dict[card] += 1

        return temp_dict

    def _judge_compare_method(self):
        '''
        判断使用那一中方法比较手牌，
        :return: 返回相应的key
        '''
        left_len = len(self.left_card)
        right_len = len(self.right_card)

        # 首先判断两手拍长度相等的情况
        if left_len == right_len:
            # 都是单个 只需要比较第一张牌
            if left_len == 1:
                return 1
            # 都有两张牌，有两张情况，都是对子，或者为两个王,但是不可能出现两个人都是两个王
            elif left_len == 2:
                # 因为我们的输入默认是已经经过排序了的，所以我们只需要知道第一张牌是否为16，如果是的话，就是双王，有双王的情况
                if self.left_card[0] == 16 or self.right_card[0] == 16:
                    return 2
                # 两个对子比较，只需要比较第一张牌的大小
                else:
                    return 1
            # 没有牌数等于三的情况,所以就跳过三张牌的情况，分析四张牌的情况。
            # 这里有三种情况，都是三带一，都是炸弹，一个炸弹一个三带一
            elif left_len == 4:
                left_max_repeat_count = max( self._get_every_value_repeat_count(self.left_card).values() )
                right_max_repeat_count = max( self._get_every_value_repeat_count(self.right_card).values() )
                # 都是三带一或者炸弹情况
                if left_max_repeat_count == right_max_repeat_count:
                    # 都是三带一的情况
                    if left_max_repeat_count == 3:
                        return 3
                    # 都是炸弹的情况，只需要比较第一张牌
                    else:
                        return 1
                # 一个三带一，一个炸弹的情况
                else:
                    return 4
            # 都是顺子的情况 最少5张牌，最多12张牌，也只需要比较第一张牌
            elif left_len >= 5 and left_len <= 12:
                return 1
            # 处理其他意外情况
            else:
                return None
        # 两手牌长度不相等的情况 必须得有一个炸弹
        else:
            # 有王炸的情况
            if left_len == 2 or right_len == 2:
                return 3
            # 没有王炸的情况,有一个炸弹的情况
            else:
                return 4

    def _compare_first_value(self):
        '''
        只需要比较第一张牌的情况
        :return: 返回较大的一手牌
        '''
        if self.left_card[0] > self.right_card[0]:
            return self.left_card
        else:
            return self.right_card

    def _compare_has_two_joker(self):
        '''
        有两个王的比较
        :return: 返回较大的一手牌
        '''
        if self.left_card[0] == 16:
            return self.left_card
        else:
            return self.right_card

    def _compare_three_with_one(self):
        '''
        比较两个三带一
        :return: 返回较大的一手牌
        '''
        left_cards_dict = self._get_every_value_repeat_count(self.left_card)
        right_cards_dict = self._get_every_value_repeat_count(self.right_card)

        left_number = right_number = 0

        for key,value in left_cards_dict.items():
            if value == 3:
                left_number = key
                break

        for key,value in right_cards_dict.items():
            if value == 3:
                right_number = key
                break

        if left_number > right_number:
            return self.left_card
        else:
            return self.right_card

    def _compare_bomb_and_others(self):
        '''
        炸弹和其他牌的比较
        :return: 返回较大的一手牌
        '''
        if max( self._get_every_value_repeat_count(self.left_card).values() ) == 4:
            return self.left_card
        else:
            return self.right_card

    def compare_two_cards(self):
        '''
        比较两副牌的大小，返回较大的一副牌
        :return:
        '''
        method_key = self._judge_compare_method()
        method = self.function_map[method_key]
        cards = method()
        cards = self._show_playing_card(cards)
        return cards


if __name__ == '__main__':

    while True:
        two_cards = input("请输入两幅手牌，中间使用-分割开，每张牌使用`,`分开：")

        left_cards = two_cards.split('-')[0].split(',')
        right_cards = two_cards.split('-')[1].split(',')

        print(left_cards,right_cards)

        compare_object = PlayingCard(left_cards,right_cards)
        result_cards = compare_object.compare_two_cards()
        print(result_cards)

        is_continue = input("是否继续：y or n : ")

        if is_continue == 'n':
            break
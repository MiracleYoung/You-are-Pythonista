class Solution:
    def solveSudoku(self, board):

        # 判断当前位置是否有数字存在
        def isvalid(board_value, i, j, num):
            # 先判断行，列固定不变
            for row in range(0, 9):
                if board_value[row][j] != ".":
                    d = int(board_value[row][j])
                    if (d == num) is True:
                        return False

            # 再判断列，行固定不变
            for col in range(0, 9):
                if board_value[i][col] != ".":
                    d = int(board_value[i][col])
                    if (d == num) is True:
                        return False

            # 9宫格中有相同的，说明尝试错误
            for row in range(i // 3 * 3, i // 3 * 3 + 3):
                for col in range(j // 3 * 3, j // 3 * 3 + 3):

                    if board_value[row][col] != ".":
                        d = int(board_value[row][col])
                        if (d == num) is True:
                            return False

            return True

        # 查找函数
        def search(board_value):
            # 总共有多少个数组
            for i in range(len(board_value)):
                # 循环每个数组
                for j in range(len(board_value[0])):
                    # 如果不是空位（即"."），则继续寻找下一个位置
                    if board_value[i][j] != ".":
                        continue

                    # 从数字1-9中依次去尝试
                    for num in range(1, 10):
                        result = isvalid(board_value, i, j, num)
                        if result is False:
                            continue

                        # 把数字填充到相应的位置
                        board_value[i][j] = num
                        # 继续寻找下一个位置
                        result = search(board_value)

                        # 如果全部执行完，都是正确，则已经完成搜索
                        if result is True:
                            return True
                        else:
                            # 回退之前的状态,本轮搜索失败,回退的时候也是递归的
                            board_value[i][j] = "."
                    else:
                        return False

            return True

        search(board)
        print(board)


s = Solution()

s.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

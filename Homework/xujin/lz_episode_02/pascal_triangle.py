import time

def get_pascal_triangle(row):
    result = [[1]]
    if row > 1:
        for _ in range(row-1):
            result.append([])

        for row in range(1,row):
            col_num = row+1
            for col in range(col_num):
                if col==0 or col == col_num-1:
                    result[row].append(1)
                else:
                    result[row].append(result[row-1][col-1] + result[row-1][col])

    return result

def show_pascal_triangle(pascal_triangle):
    row = len(pascal_triangle)
    for index,row_value in enumerate(pascal_triangle):
        print(" "*(row-index-1),end="")
        str1 = ' '.join([str(value) for value in row_value])
        print(str1)

if __name__ == '__main__':
    while True:
        row = input("请输入杨辉三角的行数：")
        try:
            row = int(row)
            break
        except ValueError:
            print("请输入格式正确的值")
            time.sleep(3)

    pascal_triangle = get_pascal_triangle(row)
    show_pascal_triangle(pascal_triangle)
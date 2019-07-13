"""
返回杨辉三角第 n 行第 k 列的值
"""


def YH_triangle(n, k):
    _k = k - 1
    tri_ls = [1]
    for i in range(n):
        tri_ls = [1] + [tri_ls[i] + tri_ls[i + 1] for i in range(len(tri_ls) - 1)] + [1]
    if len(tri_ls) > _k:
        # print(tri_ls)
        print(f"您输入的第 {n} 行第 {k} 列的元素为: {tri_ls[_k]}")
        return tri_ls[_k]
    print(f"您输入的第 {n} 行只有 {len(tri_ls)} 个元素!")


if __name__ == "__main__":
    n, k = 100, 55
    YH_triangle(n, k)
    # 结果: 您输入的第 100 行第 55 列的元素为: 73470998190814997343905056800

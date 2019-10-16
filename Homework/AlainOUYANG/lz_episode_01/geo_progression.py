'''
@Author: AlainOUYANG
@Date: 2019-10-16 16:55:11
@LastEditors: AlainOUYANG
@LastEditTime: 2019-10-16 17:14:05
@Description: geo_progression
'''
def geo_progression(a, q, n):
    if q == 1:
        S = a * n
    else:
        S = a * (q ** n - 1) / (q - 1)
    return S

def main():
    print(geo_progression(3, 2, 5))

if __name__ == "__main__":
    main()
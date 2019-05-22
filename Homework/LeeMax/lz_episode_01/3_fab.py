def fab(n):
    if n <= 2:
        return 1

    fab_list = [1,1]
    for i in range(n-2):
        fab_list.append(fab_list[-1] + fab_list[-2])

    return fab_list[-1]

if __name__ == "__main__":
    print(fab(6))
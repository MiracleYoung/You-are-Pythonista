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
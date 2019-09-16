# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt


def main():
    path = './dog/1.jpg'
    image = cv2.imread(path)
    print(image)
    plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    main()

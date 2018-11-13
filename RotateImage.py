import cv2
import math
import numpy as np

class rotator:

    height = 0
    width = 0
    angle = 90
    img = cv2.imread('lena.jpg',0)

    def __init__(self):
        pass

    def showImg(name, self):
        cv2.imshow(name, self.img)
        self.width,self.height = self.img.shape

    def printWH(self):
        print(self.width)
        print(self.height)

    def rotate(self):
        for x in range(self.width):
            for y in range(self.height):
                x = x*math.cos(self.angle)-y*math.sin(self.angle)
                y = x*math.sin(self.angle)+y*math.cos(self.angle)
        self.img.shape = self.width,self.height
        cv2.imshow('rotated', self.img.shape)

def main():
    rotator.showImg('normal', rotator)
    rotator.printWH(rotator)
    rotator.rotate(rotator)
    #rotator.showImg('rotated', rotator)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()

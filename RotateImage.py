import cv2
import math
import numpy as np

class rotator:

    height = 0
    width = 0
    angle = 90
    radians = angle*(math.pi/180)
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
        empty = np.zeros((self.height*2,self.width*2),dtype="uint8")
        for x in range(self.width):
            for y in range(self.height):
                if x<220 or y < 220:
                    #alpha = 1 * math.cos(self.radians)
                    #beta = 1 * math.sin(self.radians)
                    temp = self.img[y,x]
                    xr = x*math.cos(self.radians)-y*math.sin(self.radians)
                    yr = x*math.sin(self.radians)+y*math.cos(self.radians)

                    #xr = alpha+beta+ (1-alpha)*(self.width/2)-beta*(self.height/2)
                    #yr = -beta + alpha + beta*(self.width/2)+(1-alpha)*(self.height/2)

                    empty[int(yr),int(xr)] = temp


        cv2.imshow('rotated', empty)

def main():
    rotator.showImg('normal', rotator)
    rotator.printWH(rotator)
    rotator.rotate(rotator)
    #rotator.showImg('rotated', rotator)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()

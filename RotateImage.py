import cv2
import math
import numpy as np

class rotator:

    height = 0
    width = 0
    angle = 360
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
                if x<219 or y < 219:
                    alpha = 1 * math.cos(self.angle)
                    beta = 1 * math.sin(self.angle)
                    temp = self.img[y,x]
                    #xr = x*math.cos(self.angle)+y*math.sin(self.angle)
                    #yr =  -x*math.sin(self.angle)+y*math.cos(self.angle)

                    xr = alpha+beta+ (1-alpha)*(self.width/2)-beta*(self.height/2)
                    yr = -beta + alpha + beta*(self.width/2)+(1-alpha)*(self.height/2)

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
